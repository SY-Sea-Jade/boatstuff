---
title: Navigation Templates
toc: false
---

# Navigation Templates

```js
import SQLite from "npm:@observablehq/sqlite";
```

```js
const collection = FileAttachment("data/navigation.zip").zip();
```

```js
const options = collection.file("Tidal_Planning.db").sqlite();
```

```js
const products = options.sql`SELECT * FROM Tidal_Planning`;
await products;
```
