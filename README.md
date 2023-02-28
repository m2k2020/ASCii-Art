# ASCII Art
-----

## Dulamr / Overview
### SO 
Tool-kaan Wuxuu kaa caawin Doonaa in uu si automatic kuugu sameeyo Farshaxnka lagu Magacaabo ASCII Art, Farshaxankaan Wuxuu ka Kooban yahy summaddo/calaamado leysku geeyay waxaan isticmaala dadka programmers-ka. waxaan tool-kaan aan ku sameeyay luqadda python waxaan ka dhigay Open Source sidoo kale waxaan ugu tala galay in ay dad walba kaa faa'ideystaan. 

### EN
This tool will help you to automatically create ASCII art, this art consists of laser symbols used by programmers. I made this tool in Python language and made it Open Source and I intend for everyone to benefit from it.



## Sida Loo Isticmaalo / How to use

### SO
waxaa laga maarmaan ah in marka hore computerkaada uu kugu jiro python, haddii uusan computerkaada ku jirin luqada python fadlan kala soo dag internet-ka raac link-gaan https://www.python.org/downloads/release/python-3112/, marka uu kuu dago ka dib ku shubo kombiyuutarkaadi.
ka dib soo furo vs-code ama sublime ama wax walba aad u isticmaali karto text editor islmarkaasan waxaad ku diyaarsataa in aad ku qori karto luuqada pyhton ka dib waxaa ku dhubaneysaa Libery-ga lagu magacaabo `Pyfiglet` adoo raacaya tilmaamanta `pip install pyfiglet`.

### EN
It is necessary that you have python on your computer first, if your computer does not have python language please download it from the internet by following this link https://www.python.org/downloads/release/python-3112/, Once downloaded, Install it to your computer.
then open vs-code or sublime or anything you can use as a text editor and now you are ready to write in python language then you can install the libery called `Pyfiglet` by following the instruction `pip install pyfiglet` .



**Sida Loo Kiciyo File-ka / Running the File:**
```
py run.py -t Musharraf-Faqi
```


**Natiijada / Output :**

```

              __  __           _                           __       _____           _
             |  \/  |_   _ ___| |__   __ _ _ __ _ __ __ _ / _|     |  ___|_ _  __ _(_)
             | |\/| | | | / __| '_ \ / _` | '__| '__/ _` | |_ _____| |_ / _` |/ _` | |
             | |  | | |_| \__ \ | | | (_| | |  | | | (_| |  _|_____|  _| (_| | (_| | |
             |_|  |_|\__,_|___/_| |_|\__,_|_|  |_|  \__,_|_|       |_|  \__,_|\__, |_|
                                                                                 |_|```
```

## Qeybta Hormarinta /Development Setup

1. **Sida aad github-ka ula dagi laheed / how to clone to github**
```
git clone https://github.com/m2k2020/ASCii-Art.git
cd Desktops/projects/ASCII-Art/starter_code 
```

2.  **Markaad dhammayso  koodkaaga, waxaad ku push-gareen kartaa kaydka akoonkaaga Github adoo isticmaalaya amarada soo socda. / Once you have finished editing your code, you can push the local repository to your Github account using the following commands.**
```
git remote -v 
git remote remove origin 
git remote add origin <https://github.com/<USERNAME>/<REPO_NAME>.git>
git branch -M master

git add . --all   
git commit -m "your comment"
git push -u origin master
```