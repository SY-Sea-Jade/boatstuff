---
title: Checklists
toc: true
---

# Checklists

```js
import SQLite from "npm:@observablehq/sqlite";
```

```js
const collection = FileAttachment("data/checklists.zip").zip();
await collection;
```

```js
const master_list = collection.file("Master_List.db").sqlite();
await master_list;
```

```js
const checklist_sample = await master_list.sql`SELECT * FROM Checklist LIMIT 1`;
console.log("Checklist columns:", Object.keys(checklist_sample[0]));
```

## On the Water

### Preparing to Sail

```js
const prep = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Preparing_to_Sail = 'Y' ORDER BY Area, Task`;
await prep;
```

```js
Inputs.table(prep,{rows:24})
```

### After Sailing

```js
const after =  master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE After_Sailing = 'Y' ORDER BY Area, Task`;
await after;
```

```js
Inputs.table(after,{rows:24})
```


### Heavy Weather

```js
const heavy_weather = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Heavy_Weather_Prep = 'Y' ORDER BY Area, Task`;
await heavy_weather;
```

```js
Inputs.table(heavy_weather,{rows:24})
```
## At the Marina

### Arriving at Boat


```js
const arriving = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Arriving_On_Boat = 'Y' ORDER BY Area, Task`;
await arriving;
```

```js
Inputs.table(arriving,{rows:24})
```


### Leaving Boat

```js
const leaving = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Leaving_Boat = 'Y' ORDER BY Area, Task`;
await leaving;
```

```js
Inputs.table(leaving,{rows:24})
```

### Pontoon Storm Prep

```js
const storm = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Pontoon_Storm_Prep = 'Y' ORDER BY Area, Task`;
await storm;
```

```js
Inputs.table(storm,{rows:24})
```

### Laying Up

```js
const laying_up = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Laying_Up = 'Y' ORDER BY Area, Task`;
await laying_up;
```

```js
Inputs.table(laying_up,{rows:24})
```


### Hauled Out

```js
const hauled_out = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Hauled_Out = 'Y' ORDER BY Area, Task`;
await hauled_out;
```

```js
Inputs.table(hauled_out,{rows:24})
```

### Splashing Prep

```js
const splashing = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Splashing_Prep = 'Y' ORDER BY Area, Task`;
await splashing;
```

```js
Inputs.table(splashing,{rows:24})
```

### Engine Service

```js
const engine_service = master_list.sql`SELECT Area, Task, "Check" FROM Checklist WHERE Engine_Service = 'Y' ORDER BY Area, Task`;
await engine_service;
```

```js
Inputs.table(engine_service,{rows:24})
```
## Source Data

### All Checklists

```js
const all_of_em = master_list.sql`SELECT * FROM Checklist ORDER BY Area, Task`;
await all_of_em;
```

```js
const excluded_columns = new Set(["Check", "", "None", "null"]);
const all_of_em_columns = all_of_em.length
  ? Object.keys(all_of_em[0]).filter((c) => !excluded_columns.has(c))
  : [];
```

```js
Inputs.table(all_of_em,{rows:50, columns: all_of_em_columns, layout: "auto"})
```
### Original Spreadsheet

Use the original spreadsheet to adapt for your own use, MacOS required.

```html
📊 <a href="${await FileAttachment("numbers/checklists.numbers").url()}" download="checklists.numbers">checklists.numbers</a>
```
