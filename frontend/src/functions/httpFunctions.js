export const httpGet = async (url) => {
  const resp = await fetch(url).catch((err) => console.log(err));
  const result = await resp.json();

  if (!resp.ok) {
    console.log("An error occured.");
    return false;
  }

  return result;
};

export const httpPost = async (url, data) => {
  const resp = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  }).catch((err) => console.log(err));

  const result = await resp.json();

  if (!resp.ok) {
    console.log("An error occured.");
    console.log(result);
    return result;
  }

  return result;
};

export const httpPatch = async (url, data, etag) => {
  const resp = await fetch(url, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      "If-Match": etag,
    },
    body: JSON.stringify(data),
  }).catch((err) => console.log(err));

  const result = await resp.json();

  if (!resp.ok) {
    console.log("An error occured.");
    console.log(result);
    return result;
  }

  return result;
};

export const httpPut = async (url, data, etag) => {
  const resp = await fetch(url, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "If-Match": etag,
    },
    body: JSON.stringify(data),
  }).catch((err) => console.log(err));

  const result = await resp.json();

  if (!resp.ok) {
    console.log("An error occured.");
    console.log(result);
    return result;
  }

  return result;
};

export const httpDelete = async (url, etag) => {
  const resp = await fetch(url, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      "If-Match": etag,
    },
  }).catch((err) => console.log(err));

  if (!resp.ok) {
    console.log("An error occured.");
    console.log(resp);
    return false;
  }

  return "Item deleted successfully.";
};
