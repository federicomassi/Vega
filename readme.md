# Vega Launcher

## What it does  
Vega Launcher is a lightweight tool that keeps your **websites, applications, and files** organized and ready to launch directly from the system tray.  

## Why?  
When giving online presentations, speed and order matter. Vega Launcher helps you keep everything at your fingertips, so you can open the right apps and files without distractions.  

## How to get started  
### Run the Python files directly
You can install dependancies by `pip install PyQt5` and then run `python3 main.py` (you'll need also translations.py in the same dir).

### Use the compiled version
You can use the compiled versions available in the `/dist` folder.
In future I would provide full installation packages.

## How to customize the links
By pressing Edit in the app menu, you wull access the links.json.
Each elemant can be one in four type:
1. a submenu (containing more elements),
    ```
    ...{
    "name": "Main Menu",
    "submenu": [
      {
        ... other elements ...
      },,...
    ```
2. a URL (that will be opened in the browser),
    ```
    ...{
    "name": "Ecosia",
    "url": "https://www.ecosia.org/"
    },...
    ```
3. a cmd (that will open the choosen app)
    ```
    ...{
    "name": "GIMP",
    "cmd": "gimp"
    },...
    ```
4. a path (that will open a local file in the choosen app)
    ```
    ...{
    "name": "Generic important document 😊",
    "path": "/home/mypc/Documents/file.odt"
    },...
    ```

## Help  
- Open an issue here on GitHub if you encounter problems or have suggestions.  
- Check the documentation included in the repository.

## The project  
Vega Launcher is maintained by **Federico Massi**. Contributions are welcome — especially to improve and expand translations.  

---

## License  
This project is distributed under the **GNU GPLv3** license.  