# Discord's Game Activity Sucks (D-GAS)
*The software is still a work in progress and isn't completed yet*

- My vision for the final version is that users will be able to make and share their own presence files defining when and how DGAS should show a program on the user's profile and that DGAS will be automatically switching presences every time the user switches programs. For exam

D-GAS' main purpose is to fix Discord's bad game activity using the Rich Presence API.
If you open something like Notepad while having D-GAS running it will switch the rich presence on your profile to Notepad, listing the file you have open (and if you open another program D-GAS will search trough existing presences to use the presence for the program).

![](https://github.com/flarfmatter/dgas/blob/main/example.png)

D-GAS can currently show presences when the appropriate program is open and can stop the presence when the program is closed. It can also recognize what project/file is open in the program by grabbing the process' title.
It **cannot** switch presences automatically for now however because of a bug i'm trying to solve. (it should be able to soon enough)
