# Cowin Slot Lookup

This is a simple selenium python script that looks up available slots on the cowin website. As the website is changing daily due to bug fixes, the code is changed on a regular basis to maintain the right paths.

## Prerequisites
- [Firefox](https://www.mozilla.org/en-US/firefox/new/)


- Download the following python libraries.
(You should also be having Python3)
```
pip install selenium
pip install playsound
```

## Installation and Running

Clone the repo, cd into it, run main.py.

```
git clone https://github.com/HotMonkeyWings/AutoVax.git
cd Vax
python main.py
```

### Config

- To have a look at how the browser is working, turn headless mode off. (Option is now available on running the program)
```
fireFoxOptions.headless = False
```
- You could search by district or by PIN. (Note: District is currently only limited to Kerala. To manually change it, change the `state` paramaeter in `searchByDistrict` from 18 to your state's number in the cowin website list)

- To disable 18+ filter, comment that line out.

## Credits
Dev Sony - [@HotMonkeyWings](https://github.com/HotMonkeyWings)



