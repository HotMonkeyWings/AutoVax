# Cowin Slot Lookup

./trial.mp4

This is a simple selenium python script that looks up available slots on the cowin website. As the website is changing daily due to bug fixes, the code is changed on a regular basis to maintain the right paths.

## Prerequisites

Download the following python libraries.
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

To have a look at how the browser is working, turn headless mode off.
```
fireFoxOptions.headless = False
```

To select your own state and district, change the option numbers in placeSelector()

To disable 18+ filter, comment that line out.

## Credits
Dev Sony - [@HotMonkeyWings](https://github.com/HotMonkeyWings)



