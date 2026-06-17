---
title: Options to Integrate NMEA and Wifi
toc: false
---

# NMEA to Wifi Integration

There's a more extensive list of vendors and projects now at the [NMEA Interfacing](https://awesome-boat-tech.rhizomatics.org.uk/#nmea-interfacing) section of the [Awesome Boat Tech](https://awesome-boat-tech.rhizomatics.org.uk) list.

```js
import SQLite from "npm:@observablehq/sqlite";
```

```js
const collection = FileAttachment("data/nmea_wifi.zip").zip();
```

```js
const options = collection.file("Products.db").sqlite();
```

```js
const products = options.sql`SELECT * FROM Products`;
await products;
```

## Products

```js
const search = view(Inputs.search(products, {placeholder: "Search products ..."}));
```
```js
Inputs.table(search,{rows:20})
```

## Original Spreadsheet

Use the original spreadsheet to adapt for your own use, MacOS required.

```html
📊 <a href="${await FileAttachment("numbers/nmea_wifi_options.numbers").url()}" download="nmea_wifi_options.numbers">nmea_wifi_options.numbers</a>
```
