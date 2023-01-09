import requests
import time
import datetime
import csv
try:
    with open("./datasets/data.csv", 'w') as file:
        file.truncate(0)
        writer = csv.writer(file)
        coin_api_id = "yearn-finance"
        coin_symbol = "YFI"
        writer.writerow(["timestamp", coin_symbol + " price", "twitter followers", "reddit average posts",
                        "reddit average comments 48h", "reddit subscribers", "reddit accounts active 48h", "BTC price"])
        precio = []
        timestamp = 1641006000
        data = []
        response = requests.get(
            'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=usd&from=1641006000&to=1672542000').json()
        # print(response)
        btc_price = response['prices']
        for i in range(0, 365):
            date_obj = datetime.date.fromtimestamp(timestamp)
            month = str(date_obj.month)
            day = str(date_obj.day)
            if (len(month) == 1):
                month = '0'+month
            if (len(day) == 1):
                day = '0'+day
            response = requests.get('http://api.coingecko.com/api/v3/coins/'+coin_api_id +
                                    '/history/?date='+day+"-"+month+"-"+str(date_obj.year)).json()
            # print(response)
            if "market_data" in response:
                coin_price = response['market_data']['current_price']['usd']
                coin_market_cap = response['market_data']['market_cap']['usd']
                coin_total_volume = response['market_data']['total_volume']['usd']
                if response['community_data']['twitter_followers']:
                    twitter_followers = response['community_data']['twitter_followers']
                reddit_average_posts_48h = response['community_dapta']['reddit_average_posts_48h']
                reddit_average_comments_48h = response['community_data']['reddit_average_comments_48h']
                reddit_subscribers = response['community_data']['reddit_subscribers']
                reddit_accounts_active_48h = response['community_data']['reddit_accounts_active_48h']
                print(date_obj, coin_price, "\n")
                timestamp += 86400
                writer.writerow([date_obj, coin_price, twitter_followers, reddit_average_posts_48h,
                                reddit_average_comments_48h, reddit_subscribers, reddit_accounts_active_48h, btc_price[i][1]])
            else:
                time.sleep(65)
            print("aproximately "+str((365-i)*10/60)+" minutes remaining")
            time.sleep(10)
except NameError:
    print(NameError)
    pass

print(file.closed)