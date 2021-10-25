import pandas as pd
import datetime
from eve import Eve
from flask import current_app as capp
from flask import request, send_file

def calculate_total_consumption(item):
    """Calculate total consumptions."""
    consumptions = ['water_consumption', 'power_consumption', 'thermal_consumption']
    # loop through consumptions
    if 'cost' not in item:
        return

    cost_total = 0
    for c in consumptions:
        # check requirements 
        if c not in item['cost']:
            continue
        # init the total counter
        total = 0
        for i in item['cost'][c]:
            # add value to total
            total += float(str(item['cost'][c][i]))
        # assign value to item
        item['cost'][c]['_total'] = total
        cost_total += total
    item['cost']['_total'] = cost_total
    return item

def calculate_totals(resource, response):
    """Calculate totals."""
    for item in response['_items']:
        calculate_total_consumption(item)
    return

app = Eve()
app.on_fetched_resource += calculate_totals 

KPIS = ["cost", "safety", "production", "wow"]

def datetime_to_date(dt):
    return datetime.date(dt.year, dt.month, dt.day)

def create_workbook(data, focus, filename):
    groups = {}
    # seperate groups to be written into seperate sheets
    for item in data:
        sd = datetime_to_date(item["start_date"])
        wk = item["week"]
        for key, group in item[focus].items():
            if key.startswith("_"):
                continue
            if key not in groups:
                groups[key] = []
            d = {"start_date": sd, "week": wk}
            d.update(group)
            groups[key].append(d)
    # crete excel writer object
    with pd.ExcelWriter(filename) as writer:
        for sheet, group in groups.items():
            pd.DataFrame(group).to_excel(writer, sheet_name=sheet)
    return

@app.route("/export", methods=["GET"])
def export_file():
    """File export function."""
    # datetime vars
    now = datetime.datetime.now()
    year = now.year
    # get query parameters
    resource = request.args.get("resource")
    focus = request.args.get("focus")
    start = request.args.get("start")
    end = request.args.get("end")
    # get resource from db
    data = capp.data.driver.db[resource]
    # check if start date and set it
    if not start:
        # if start not set, set start to beginning of this year
        start = datetime.datetime(year, 1, 1) 
    else: 
        start = datetime.datetime.strptime(start, "%Y-%m-%d")
    # check for an end
    if end:
        # if end present set it in the query
        end = datetime.datetime.strptime(start, "%Y-%m-%d")
    # get data aggregate
    data = list(data.aggregate([
        {"$addFields": {
            "start_date": "$date.start",
            "week": "$date.week"
        }},
        {"$project": {"start_date": 1 , "week": 1, focus: 1}}
    ]))
    # return if no data
    if len(data) == 0:
        return "No Data to Export."
    # create workbook
    create_workbook(data, focus, "/download.xlsx")
    # convert to excel using pandas data frame
    response = send_file("/download.xlsx")
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5600) 