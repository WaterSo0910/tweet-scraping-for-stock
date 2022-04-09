echo -n "Download all package you need (y/n) " 
read choice 
# source tweet-venv/Scripts/activate
if [ $choice = "y" ]
then
    pip install -r requirements.txt
    cd twint
    pip install . -r requirements.txt
    cd ..
fi
echo -n "Ready to get tweets (y/n)? " 
read choice 
if [ $choice = "y" ]
then
    echo -e "(๑•̀ㅂ•́)و✧ Let's do it!!" 
else
    echo -e "○|￣|_=3 Eat poo poo" 
    exit 0
fi
echo -n "Enter target? " 
read target 
echo -n "Enter year? (no 2022) " 
read year 
echo "Scraping popular tweets about $target in $year . . ."
for i in {1..12}
do
    python tweet_scrapy.py --search="$target" --year="$year" --month="$i" --max_nums=100
done
$SHELL