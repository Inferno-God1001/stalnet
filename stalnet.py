import sys, re, requests, tikcheck, notify, random, os
from datetime import datetime
from rich import print
from cockroach import instagram


sm_geral = [
    "tiktok",
]

usernamesRD = [
    "julius.u",
    "saitamajhh",
    "jesusfan",
    "antisocial",
    "alanzoka",
    "goularte",
    "renan2323",
    "tgool",
    "mauteodor",
    "teodorus",
    "sophia"
]

usernames = random.choice(usernamesRD)

sl = f'"python3 stalnet.py {sm_geral} {usernames}"'



if sys.version_info[0] < 3:
    print(f'[red bold]The stalnet.py file needs to be initialized by writing python3.\nSolution: {sl}')
    exit()




try:
    sm = sys.argv[1].lower()
except:     
    print(f'The social media field cannot be empty.\nSolution: {sl}')     
    exit() 


try:
    username = sys.argv[2].lower()
except:
    print(f'The username is empty. You need to put something there.\nSolution: {sl}')    
    exit()

try:
    particle = sys.argv[3].lower()
    command = sys.argv[4].lower()
    
    if particle == "-c" and command == "clear":
        os.system("cls" if os.name == "nt" else "clear")
             
    else:
        print("[red bold]This command does not exist.")    
        exit()
except:
    pass        



offline_msg = f'\n[red bold]{sm} system offline[/red bold]\n[yellow bold]system:[/yellow bold] The account named "{username}" was not found.'

online_msg = f'\n[green bold]{sm} system online[/green bold]\n\n[blue]Log:'



def Start():
    print("""[blue]
 .▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▌   ▐ ▄ ▄▄▄ .▄▄▄▄▄
 ▐█ ▀. •██  ▐█ ▀█ ██•  •█▌▐█▀▄.▀·•██
 ▄▀▀▀█▄ ▐█.▪▄█▀▀█ ██▪  ▐█▐▐▌▐▀▀▪▄ ▐█.▪
 ▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█▌▐▌██▐█▌▐█▄▄▌ ▐█▌·
  ▀▀▀▀  ▀▀▀  ▀  ▀ .▀▀▀ ▀▀ █▪ ▀▀▀  ▀▀▀
              By Inferno
            version 0.1.0""")

    if sm == "tiktok":
        tk_process = tikcheck.function.search(username)
        
        if tk_process == "found":
            print(online_msg)
            
            html_old = requests.get(f"https://tiktok.com/@{username}").text


            displayN_old = re.search(r'"nickname":"(.*?)"', html_old).group(1)
            
            userN_old = re.search(r'"uniqueId":"(.*?)"', html_old).group(1)

            bio_old = re.search(r'"signature":"(.*?)"', html_old).group(1)

            follower_old = re.search(r'"followerCount":(\d+)', html_old).group(1)

            following_old = re.search(r'"followingCount":(\d+)', html_old).group(1)

            video_old = int(re.search(r'"videoCount":(\d+)', html_old).group(1))

            while True:
                try:
                    hour = datetime.now().hour
                    minute = datetime.now().minute
                    sec = datetime.now().second

                    date = f"{hour}:{minute}:{sec}"


            
                    html = requests.get(f"https://tiktok.com/@{username}").text

                
                    displayN = re.search(r'"nickname":"(.*?)"', html).group(1)
                    
                    userN = re.search(r'"uniqueId":"(.*?)"', html).group(1)

                    bio = re.search(r'"signature":"(.*?)"', html).group(1)

                    follower = re.search(r'"followerCount":(\d+)', html).group(1)

                    following = re.search(r'"followingCount":(\d+)', html).group(1)

                    video = int(re.search(r'"videoCount":(\d+)', html).group(1))
        

                
                    if displayN == displayN_old:
                        pass
                    else:
                        displayN_msg = f"({date}) {username} changed the display name to: {displayN}."
                        print("》", displayN_msg)
                        notify.send(title="Stalnet", content=displayN_msg, icon="info")
                        displayN_old = displayN                       
                        pass
                        


                    if userN == userN_old:
                        pass
                    else:
                        userN_msg = f"({date}) {username} changed username to: {userN}." 
                        print("》", userN_msg)
                        notify.send(title="Stalnet", content=userN_msg, icon="info")
                        userN_old = userN 
                        pass


                    if bio == bio_old:
                        pass
                    else:
                        bio_msg = f"({date}) {username} changed bio to: {bio}"   
                        print("》", bio_msg)
                        notify.send(title="Stalnet", content=bio_msg, icon="info")
                        bio_old = bio
                        pass



                    if follower == follower_old:
                        pass
                    else:
                        follower_msg = f"({date}) The {username} gained another follower: {follower}"    
                        print("》", follower_msg)
                        notify.send(title="Stalnet", content=follower_msg, icon="info")
                        follower_old = follower
                        pass

                    if following == following_old:
                        pass
                    else:
                        following_msg = f"({date}) The user is now following {following} people."  
                        print("》", following_msg)  
                        notify.send(title="Stalnet", content=following_msg, icon="info")
                        following_old = following
                        pass



                    if video == video_old:
                        pass
                    else:
                        if video > video_old:
                            video_msg_o = f"({date}) The {username} posted another video and now has {video} videos"   
                            
                            print("》", video_msg_o)     
                            notify.send(title="Stalnet", content=video_msg_o, icon="info")
                            video_old = video
                                
                            pass
                        else:
                            video_msg_t = f"({date}) The {username} deleted one video and now has {video} videos."
                            print("》", video_msg_t)
                            notify.send(title="Stalnet", content=video_msg_t, icon="info")   
                            video_old = video 
                            pass
                    
                    
                except Exception as e:      
                    print(e)
                    notify.send(title="Stalnet", content=f"error: {e}", icon="warning")
                    exit()
                    break




        else:
            print(offline_msg)
            exit()
            

    else:
        print(f'[yellow]The social network called "{sm}" is not on our list of social networks that work in our script.\nSolution: {sl}')            
        exit()

             
Start()
