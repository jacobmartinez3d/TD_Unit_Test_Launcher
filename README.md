# Touch Designer Unit-Test-Launcher.

Launch Touch Designer from the command-line or terminal, trigger python scripts to run on startup, and close with optional callback on exit.


## Getting Started

Clone or download this repository.

The default settings in *config.txt* point to *example_test_folder* as the target directory containing .py files to run inside Touch Designer, but you can point to any other directory by pasting an absolute path instead. A result log will always be saved inside the folder you target. The log name can also be set in config.txt.


#### In order for the exit callback to work, it requires making a slight edit to:
*/Touch/Designer/Install/Location/bin/TouchInit.py*.

Change the *exit()* definition toward the end of *TouchInit.py* from:
```
def exit():

    project.quit()
```
to:

```
def exit(callback_, arg):

    callback_(arg)

    project.quit()
```
Now your exit callback code will run just before the exit command.


### Prerequisites

Must have Touch Designer installed


### Running

To run, open a CMD prompt or terminal window.

Run *unit_test_launcher.toe* with the Touch Designer execute-able.

example in Windows:
```
"C:\Program Files\Derivative\TouchDesigner099\bin\TouchDesigner099.exe" "E:\Projects\TDGam\tests\unit_test_launcher.toe"
```

Touch Designer will launch, import the python files as modules in your target folder, write to a txt log, then exit and open the report log.


## Authors

* **Jacob Martinez** - *Pipeline TD* - [Magnetic-Lab](https://www.magnetic-lab.com)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
