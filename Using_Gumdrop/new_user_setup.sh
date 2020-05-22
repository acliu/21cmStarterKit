# This isn't meant for public cosumption. It's just what Adrian
# has to run to create new accounts on Gumdrop, and he's putting
# it here so that he doesn't lose it

username="hannahf"
fullname="Hannah Fronenberg"
default_pw="rutherford"
user_id='531'
group_id='20'

sudo dscl . -create /Users/$username
sudo dscl . -create /Users/$username UserShell /bin/bash
str="sudo dscl . -create /Users/$username RealName \"$fullname\""
eval $str
sudo dscl . -create /Users/$username UniqueID $user_id
sudo dscl . -create /Users/$username PrimaryGroupID $group_id
sudo dscl . -create /Users/$username NFSHomeDirectory /Users/$username
sudo mkdir /Users/$username
sudo chown -Rv $username /Users/$username
sudo dscl . -passwd /Users/$username $default_pw

