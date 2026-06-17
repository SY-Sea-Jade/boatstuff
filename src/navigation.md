---
title: Navigation Templates
toc: false
---

# Navigation Templates

## Tidal Planner

Used to plan viable times for tight tidal gates, like the notorious Mull of Kintyre.

```html
📄 <a href="${await FileAttachment("pdf/navigation_templates.pdf").url()}" download="navigation_templates.pdf">navigation_templates.pdf</a>
```

```html
<iframe
  src="${await FileAttachment("pdf/navigation_templates.pdf").url()}"
  width="100%"
  height="900px"
  style="border: none;"
></iframe>
```

## Original Spreadsheet

Use the original spreadsheet to adapt for your own use, MacOS required.

```html
📊 <a href="${await FileAttachment("numbers/navigation.numbers").url()}" download="navigation.numbers">navigation.numbers</a>
```
