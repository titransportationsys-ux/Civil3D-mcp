# Alignment Review Desk: review page

Single-file page: pan/zoom map, findings, sign table with Keep/Fix/Remove decisions, master catalogue, Setup, Export and Methods tabs.

```bash
python dashboard/extract_data.py --network-dxf Wyte.dxf --signing-dxf Wyte_Signing_1.dxf   # writes dashboard/data.json (Wyte demo data is already included)
python dashboard/build.py                                                                   # writes dashboard/index.html
NODE_PATH=$(npm root -g) node dashboard/test.cjs                                             # headless check
```

`index.html` is generated; publish it as the page. The page reads a loaded DXF in the browser, so `data.json` only supplies the demo, the catalogue, the block map and the links.
