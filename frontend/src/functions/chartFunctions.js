import colors from "vuetify/lib/util/colors";

const BORDER_WIDTH = 4;
const OVER_TARGET_COLOR = "red";
const COLOR_KEYS = ["green", "blue", "yellow", "teal", "purple"];

function axisKeyToArray(key) {
  return key.split(".");
}

function getDataFromAxisKey(axisKey, data) {
  const keys = axisKeyToArray(axisKey);
  var d = data;
  for (const i in keys) {
    if (!(keys[i] in d)) {
      continue;
    }
    d = d[keys[i]];
  }
  return d;
}

export const setTarget = (targets, condition, datasets, resource) => {
  let t = [];
  for (const i in datasets) {
    var target = targets.filter(item => item.resource === resource && item.target_name === datasets[i].title)
    if (!target) {
      target = 0;
    }
    const normColor = getRandomChartColor(i);
    datasets[i].backgroundColor = normColor;
    switch (condition) {
      case "gt":
        setGreaterThanColor(datasets[i], target, normColor);
        break;
      case "lt":
        setLessThanColor(datasets[i], target, normColor);
        break;
    }
    t.push({ x: "target", y: target });
  }
  datasets.push({ data: t, type: "line", label: "Target" });
};

export const setGreaterThanColor = (dataset, target, normColor) => {
  if (!("borderWidth" in dataset)) {
    dataset.borderWidth = [];
  }
  if (!("borderColor" in dataset)) {
    dataset.borderColor = [];
  }
  for (const i in dataset.data) {
    const value = getDataFromAxisKey(dataset.parsing.yAxisKey, dataset.data[i]);
    console.log("VALUE --->", value);
    console.log("TARGET --->", target);
    if (value > target) {
      dataset.borderWidth.push(BORDER_WIDTH);
      dataset.borderColor.push(OVER_TARGET_COLOR);
    } else {
      dataset.borderWidth.push(BORDER_WIDTH);
      dataset.borderColor.push(normColor);
    }
  }
};

export const setLessThanColor = (dataset, target, normColor) => {
  if (!("borderWidth" in dataset)) {
    dataset.borderWidth = [];
  }
  if (!("borderColor" in dataset)) {
    dataset.borderColor = [];
  }
  for (const i in dataset.data) {
    const value = getDataFromAxisKey(dataset.parsing.yAxisKey, dataset.data[i]);
    if (value > target) {
      dataset.borderColor.push(OVER_TARGET_COLOR);
      dataset.borderWidth.push(BORDER_WIDTH);
    } else {
      dataset.borderWidth.push(BORDER_WIDTH);
      dataset.borderColor.push(normColor);
    }
  }
};

export const getRandomChartColor = (i) => {
  const color = colors[COLOR_KEYS[i]];
  return color.base;
};
