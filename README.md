# Otter API

__An API for serving otter photos.__
https://otters.up.railway.app/
This api was made originally [here](https://github.com/Player1041/old-animal-pics-api) but it had issues, so I rewrote it to work a bit better.

## Documentation

`/` - Base url, just to check the site is up tbh.  
`/otter` - Returns JSON data containing a random URL to the photo under `otter_url` along with a number so under `otter_number` so the user can use it to call a specific photo if you wish to implement it.  
`/otter?photo=int` - Replace `int` with a number and it becomes `/otter` without the randomization.  
`/otter/int` - The image URl, replace `int` with a number and it will be as an image URL.  

Enjoy!
(If you wish to submit photos, either make a pull request and name the files numerically OR add me on Discord @Player1041#3716 and send me them there and I'll add them. No duplicates though.)
