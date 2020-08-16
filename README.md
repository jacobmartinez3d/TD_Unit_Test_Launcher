# Touch Designer Unit-Test-Launcher.

Launch Touch Designer from the command-line or terminal, trigger python unittest scripts to run on startup, and close with optional callback on exit.


## Getting Started

Clone or download this repository.

The default settings in *config.json* point to *example_test_folder* as the target directory containing TestCase .py files to run inside Touch Designer, but you can point to any other directory by pasting an absolute path instead.


### Prerequisites

Must have Touch Designer installed


### Running

To run, open a CMD prompt or terminal window.

Run *unit_test_launcher.toe* with the Touch Designer execute-able.

example in Windows:
```cmd
"C:\Program Files\Derivative\TouchDesigner099\bin\TouchDesigner099.exe" "E:\Projects\TDGam\tests\unit_test_launcher.toe"
```

Touch Designer will launch, import the TestCases as a TestSuite in your target folder, then exit.


## Authors

* **Jacob Martinez** - *Pipeline TD* - [Magnetic-Lab](https://www.magnetic-lab.com)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
