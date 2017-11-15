chmod +x gitc.sh
rm -rf ~/.gitc
mkdir ~/.gitc
cp gitc.sh ~/.gitc/main.sh
echo "Adding Aliases"
echo "alias gitc='bash ~/.gitc/main.sh'" >> ~/.bashrc #works for most people
echo "alias gitc='bash ~/.gitc/main.sh'" >> ~/.bash_profile #for mac
echo "alias gitc='bash ~/.gitc/main.sh'" >> ~/.zshrc #for people using oh-my-zsh
echo "alias gitc='bash ~/.gitc/main.sh'" >> ~/.profile #for everyone people

echo "Sourcing Aliases"
source ~/.bashrc
source ~/.bash_profile
source ~/.zshrc
source ~/.profile
