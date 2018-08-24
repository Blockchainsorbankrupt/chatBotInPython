#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,psycopg2
import datetime 
import requests
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import json
import random
from binance.client import Client

import infolib
import tradelib
import indexlib
import misclib







SECRET_KEY=('HIDDEN')
API_KEY=('HIDDEN')
client=Client(API_KEY,SECRET_KEY)


DB_NAME=('HIDDEN')
DB_USERNAME=('HIDDEN')
DB_HOST=('HIDDEN')
DB_PASSWORD=('HIDDEN')
DB_URL="dbname='"+DB_NAME+"' user='"+DB_USERNAME+"' host='"+DB_HOST+"' password='"+DB_PASSWORD+"'"

conn=psycopg2.connect(DB_URL)
cur=conn.cursor()
cur.execute("SELECT chat_id FROM users")
users=cur.fetchall()
id_list=[chat_id[0] for chat_id in users]
cur.close()
conn.close()

ADMIN_ID=('postgres')
ADMIN_USERNAME=('postgres')






# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def coin(bot, update,args):
    if args[-1] == '1':
        coin_list=args[:-1]
        opt=1
    else:
        coin_list=args
        opt=0
    for coinName in coin_list:
        market=infolib.getMarket(coinName)
        msg=tradelib.trade_analysis_500(client,market,opt)
        update.message.reply_text(msg,parse_mode=ParseMode.MARKDOWN)





def btcCap (bot, update):
    btcCapJson = requests.get("https://api.coingecko.com/api/v3/global").json()
    btc = btcCapJson ['data']['market_cap_percentage']['btc']
    volbtc = btcCapJson ['data']['total_volume']['btc']
    update.message.reply_text("Btc Market Cap  " + (str (btc))+'%'+
                              "              Current Volume is:  ${:,}".format(volbtc))




def ethCap (bot, update):
    ethCapJson = requests.get("https://api.coingecko.com/api/v3/global").json()
    eth = ethCapJson ['data']['market_cap_percentage']['eth']
    update.message.reply_text("ETH market cap is : "+str (int( eth))+"%")
    






def infoCoin(bot,update,args,total_string_length_to_send=470):
    if args[-1] == '1':
        coin_list=args[:-1]
        opt=1
    else:
        coin_list=args
        opt=0
    for coinName in coin_list:
        coinCall =requests.get("https://api.coingecko.com/api/v3/coins/"+str(coinName)).json()
        coinIsd = coinCall ['description']['en'][:total_string_length_to_send]
        devScore = coinCall ['developer_score']
        webPage = coinCall ['links']['homepage']
        print(coinIsd)
        update.message.reply_text("The developement score ranks: {:,}".format(devScore)+
                                  "             Webpage: "+str(webPage))
        update.message.reply_text(coinIsd,parse_mode=ParseMode.MARKDOWN)





        
def eosChange(bot, update):
    eosChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=EOS&tsyms=USD,EUR").json()
    eosChange = eosChangeCallJson['RAW']['EOS']['USD']['CHANGE24HOUR']
    eosVol = eosChangeCallJson ['RAW']['EOS']['USD']['TOTALVOLUME24HTO']
    eosPrice = eosChangeCallJson ['RAW']['EOS']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $" + str (eosChange)+
                              "              Volume for 24 hours :  ${:,}".format(eosVol)+
                              "              The price of the coin is:   ${:,}".format(eosPrice))



def nemChange(bot, update):
    nemChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=XEM&tsyms=USD,EUR").json()
    nemChange = nemChangeCallJson['RAW']['XEM']['USD']['CHANGE24HOUR']
    nemVol = nemChangeCallJson ['RAW']['XEM']['USD']['TOTALVOLUME24HTO']
    nemPrice = nemChangeCallJson ['RAW']['XEM']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $" + str (nemChange)+
                              "              Volume for 24 hours :  ${:,}".format(nemVol)+
                              "              The price of the coin is:   ${:,}".format(nemPrice))





def btcChange(bot, update):
    """Send a message when the command /start is issued."""
    btcChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC&tsyms=USD,EUR").json()
    btcChange = btcChangeCallJson['RAW']['BTC']['USD']['CHANGE24HOUR']
    btcVol = btcChangeCallJson ['RAW']['BTC']['USD']['TOTALVOLUME24HTO']
    btcPrice = btcChangeCallJson ['RAW']['BTC']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $" + str (btcChange)+
                              "              Volume for 24 hours :  ${:,}".format(btcVol)+
                              "              The price of the coin is:   ${:,}".format(btcPrice))

 


def etcChange(bot, update):
    etcChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETC&tsyms=USD,EUR").json()
    etcChange = etcChangeCallJson['RAW']['ETC']['USD']['CHANGE24HOUR']
    etcVol = etcChangeCallJson ['RAW']['ETC']['USD']['TOTALVOLUME24HTO']
    etcPrice = etcChangeCallJson ['RAW']['ETC']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $" + str (etcChange)+
                              "              Volume for 24 hours :  ${:,}".format(etcVol)+
                              "              The price of the coin is:   ${:,}".format(etcPrice))

def ethChange(bot, update):
    ethChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD,EUR").json()
    ethChange = ethChangeCallJson['RAW']['ETH']['USD']['CHANGE24HOUR']
    ethVol = ethChangeCallJson ['RAW']['ETH']['USD']['TOTALVOLUME24HTO']
    ethPrice = ethChangeCallJson ['RAW']['ETH']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $" + str (ethChange)+
                              "              Volume for 24 hours :  ${:,}".format(ethVol)+
                              "              The price of the coin is:   ${:,}".format(ethPrice))


def etpChange(bot, update):
    etpChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETP&tsyms=USD,EUR").json()
    etpChange = etpChangeCallJson['RAW']['ETP']['USD']['CHANGE24HOUR']
    etpVol = etpChangeCallJson ['RAW']['ETP']['USD']['TOTALVOLUME24HTO']
    etpPrice = etpChangeCallJson ['RAW']['ETP']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $" + str (etpChange)+
                              "              Volume for 24 hours :  ${:,}".format(etpVol)+
                              "              The price of the coin is:   ${:,}".format(etpPrice))



def bnbChange(bot, update):
    bnbChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BNB&tsyms=USD,EUR").json()
    bnbChange = bnbChangeCallJson['RAW']['BNB']['USD']['CHANGE24HOUR']
    bnbVol = bnbChangeCallJson ['RAW']['BNB']['USD']['TOTALVOLUME24HTO']
    bnbPrice = bnbChangeCallJson ['RAW']['BNB']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $" + str (bnbChange)+
                              "                  Volume for 24 hours :  ${:,}".format(bnbVol)+
                              "                  The price of the coin is:   ${:,}".format(bnbPrice))


    

def batChange(bot, update):
    """Send a message when the command /start is issued."""
    batChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BAT&tsyms=USD,EUR").json()
    batChange = batChangeCallJson['RAW']['BAT']['USD']['CHANGE24HOUR']
    update.message.reply_text("Price change over 24H: " + str (batChange))



def ltcChange(bot, update):
    """Send a message when the command /start is issued."""
    ltcChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=LTC&tsyms=USD,EUR").json()
    ltcChange = ltcChangeCallJson['RAW']['LTC']['USD']['CHANGE24HOUR']
    ltcVol = ltcChangeCallJson ['RAW']['LTC']['USD']['TOTALVOLUME24HTO']
    update.message.reply_text("Price change over 24H: " + str (ltcChange)+
                              "              Volume (in usd) for 24 hours :  "  +str(ltcVol))



def ltcChange(bot, update):
    """Send a message when the command /start is issued."""
    ltcChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=LTC&tsyms=USD,EUR").json()
    ltcChange = ltcChangeCallJson['RAW']['LTC']['USD']['CHANGE24HOUR']
    ltcVol = ltcChangeCallJson ['RAW']['LTC']['USD']['TOTALVOLUME24HTO']
    update.message.reply_text("Price change over 24H: " + str (ltcChange)+
                              "              Volume (in usd) for 24 hours :  "  +str(ltcVol))

def gntChange (bot, update):
    """Send a message when the command /start is issued."""
    gntChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=GNT&tsyms=USD,EUR").json()
    gntChange = gntChangeCallJson['RAW']['GNT']['USD']['CHANGE24HOUR']
    gntVol = gntChangeCallJson ['RAW']['GNT']['USD']['TOTALVOLUME24HTO']
    gntPrice = gntChangeCallJson ['RAW']['GNT']['USD']['PRICE']
    update.message.reply_text("Price change over 24H: " + str (gntChange)+
                              "              Volume (in usd) for 24 hours :  "  +str(gntVol)+
                              " The price of the coin is: "+ str(gntPrice))



def ontChange (bot, update):
    """Send a message when the command /start is issued."""
    ontChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ONT&tsyms=USD,EUR").json()
    ontChange = ontChangeCallJson['RAW']['ONT']['USD']['CHANGE24HOUR']
    ontVol = ontChangeCallJson ['RAW']['ONT']['USD']['TOTALVOLUME24HTO']
    ontPrice = ontChangeCallJson ['RAW']['ONT']['USD']['PRICE']
    update.message.reply_text("Price change over 24H: " + str (ontChange)+
                              "              Volume (in usd) for 24 hours :  "  +str(ontVol)+
                              " The price of the coin is: "+ str(ontPrice))






def ontChange (bot, update):
    """Send a message when the command /start is issued."""
    ontChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ONT&tsyms=USD,EUR").json()
    ontChange = ontChangeCallJson['RAW']['ONT']['USD']['CHANGE24HOUR']
    ontVol = ontChangeCallJson ['RAW']['ONT']['USD']['TOTALVOLUME24HTO']
    ontPrice = ontChangeCallJson ['RAW']['ONT']['USD']['PRICE']
    update.message.reply_text("Price change over 24H: " + str (ontChange)+
                              "              Volume (in usd) for 24 hours :  "  +str(ontVol)+
                              " The price of the coin is: "+ str(ontPrice))

    




def stormChange (bot,update):
    """Send a message when the command /start is issued."""
    stormChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=STORM&tsyms=USD,EUR").json()
    stormChange = stormChangeCallJson['RAW']['STORM']['USD']['CHANGE24HOUR']
    stormVol = stormChangeCallJson ['RAW']['STORM']['USD']['TOTALVOLUME24HTO']
    stormPrice = stormChangeCallJson ['RAW']['STORM']['USD']['PRICE']
    update.message.reply_text("Price change over 24H: $" + str (stormChange)+
                              "              Volume for 24 hours : $"  +str(stormVol)+
                              " The price of the coin is: $"+ str(stormPrice))






def dcrChange (bot,update):
    """Send a message when the command /start is issued."""
    dcrChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=DCR&tsyms=USD,EUR").json()
    dcrChange = dcrChangeCallJson['RAW']['DCR']['USD']['CHANGE24HOUR']
    dcrVol = dcrChangeCallJson ['RAW']['DCR']['USD']['TOTALVOLUME24HTO']
    dcrPrice = dcrChangeCallJson ['RAW']['DCR']['USD']['PRICE']
    update.message.reply_text("Price change over 24H: $" + str (dcrChange)+
                              "              Volume for 24 hours :  $"  +str(dcrVol)+
                              "              The price of the coin is: $"+ str(dcrPrice))




def trxChange (bot,update):
    """Send a message when the command /start is issued."""
    trxChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=TRX&tsyms=USD,EUR").json()
    trxChange = trxChangeCallJson['RAW']['TRX']['USD']['CHANGE24HOUR']
    trxVol = trxChangeCallJson ['RAW']['TRX']['USD']['TOTALVOLUME24HTO']
    trxPrice = trxChangeCallJson ['RAW']['TRX']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $" + str (trxChange)+
                              "              Volume for 24 hours :  $"  +str(trxVol)+
                              "              The price of the coin is:   $"+ str(trxPrice))


def vetChange (bot,update):
    """Send a message when the command /start is issued."""
    vetChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=VET&tsyms=USD,EUR").json()
    vetChange = vetChangeCallJson['RAW']['VET']['USD']['CHANGE24HOUR']
    vetVol = vetChangeCallJson ['RAW']['VET']['USD']['TOTALVOLUME24HTO']
    vetPrice = vetChangeCallJson ['RAW']['VET']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $" + str (vetChange)+
                              "              Volume for 24 hours :  $"  +str(vetVol)+
                              "              The price of the coin is:   $"+ str(vetPrice))




def zrxChange (bot,update):
    """Send a message when the command /start is issued."""
    zrxChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ZRX&tsyms=USD,EUR").json()
    zrxChange = zrxChangeCallJson['RAW']['ZRX']['USD']['CHANGE24HOUR']
    zrxVol = zrxChangeCallJson ['RAW']['ZRX']['USD']['TOTALVOLUME24HTO']
    zrxPrice = zrxChangeCallJson ['RAW']['ZRX']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $ {:,}".format(zrxChange)+
                              "              Volume for 24 hours : {:,} $".format(zrxVol)+
                              "              The price of the coin is: {:,}  $".format(zrxPrice))





def iotaChange (bot,update):
    """Send a message when the command /start is issued."""
    iotaChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=IOTA&tsyms=USD,EUR").json()
    iotaChange = iotaChangeCallJson['RAW']['IOTA']['USD']['CHANGE24HOUR']
    iotaVol = iotaChangeCallJson ['RAW']['IOTA']['USD']['TOTALVOLUME24HTO']
    iotaPrice = iotaChangeCallJson ['RAW']['IOTA']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $ {:,}".format(iotaChange)+
                              "              Volume for 24 hours : {:,} $".format(iotaVol)+
                              "              The price of the coin is: {:,}  $".format(iotaPrice))




def edoChange (bot,update):
    """Send a message when the command /start is issued."""
    edoChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=EDO&tsyms=USD,EUR").json()
    edoChange = edoChangeCallJson['RAW']['EDO']['USD']['CHANGE24HOUR']
    edoVol = edoChangeCallJson ['RAW']['EDO']['USD']['TOTALVOLUME24HTO']
    edoPrice = edoChangeCallJson ['RAW']['EDO']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $ {:,}".format(edoChange)+
                              "              Volume for 24 hours : {:,} $".format(edoVol)+
                              "              The price of the coin is: {:,}  $".format(edoPrice))




def neoChange (bot,update):
    """Send a message when the command /start is issued."""
    neoChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=NEO&tsyms=USD,EUR").json()
    neoChange = neoChangeCallJson['RAW']['NEO']['USD']['CHANGE24HOUR']
    neoVol = neoChangeCallJson ['RAW']['NEO']['USD']['TOTALVOLUME24HTO']
    neoPrice = neoChangeCallJson ['RAW']['NEO']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $ {:,}".format(neoChange)+
                              "              Volume for 24 hours : {:,} $".format(neoVol)+
                              "              The price of the coin is: {:,}  $".format(neoPrice))







def adaChange (bot,update):
    """Send a message when the command /start is issued."""
    adaChangeCallJson = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ADA&tsyms=USD,EUR").json()
    adaChange = adaChangeCallJson['RAW']['ADA']['USD']['CHANGE24HOUR']
    adaVol = adaChangeCallJson ['RAW']['ADA']['USD']['TOTALVOLUME24HTO']
    adaPrice = adaChangeCallJson ['RAW']['ADA']['USD']['PRICE']
    update.message.reply_text("Price change over 24H:  $ {:,}".format(adaChange)+
                              "              Volume for 24 hours : {:,} $".format(adaVol)+
                              "              The price of the coin is: {:,}  $".format(adaPrice))


    

    

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Call commands using your coin, try:  | /btc  ,  /(coin)24 , /news !!!!PLEASE DO /rules BEFORE ANYTHING!!!, /wall (coin)example: /wall eos  , /info (coinFull)example: /info bitcoin , /btccap  , /ethcap')

    



def btc(bot, update):
    """Send a message when the command /btc is issued."""
    tickCall = "https://api.bitfinex.com/v1/pubticker/btcusd"
    tickCallJson = requests.get(tickCall).json()
    tickOut = tickCallJson 
    update.message.reply_text(tickOut)




def eth(bot, update):
    """Send a message when the command /eth is issued."""
    ethtickCall = "https://api.bitfinex.com/v1/pubticker/ethusd"
    ethtickCallJson = requests.get(ethtickCall).json()
    ethtickOut = ethtickCallJson 
    update.message.reply_text(ethtickOut)






def bnb(bot, update):
    """Send a message when the command /eth is issued."""
    bnbtickCall = "https://min-api.cryptocompare.com/data/price?fsym=BNB&tsyms=USD,JPY,EUR"
    bnbtickCallJson = requests.get(bnbtickCall).json()
    bnbtickOut = bnbtickCallJson 
    update.message.reply_text(bnbtickOut)



def xrp(bot, update):
    """Send a message when the command /eth is issued."""
    xrptickCall = "https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,JPY,EUR"
    xrptickCallJson = requests.get(xrptickCall).json()
    xrptickOut = xrptickCallJson 
    update.message.reply_text(xrptickOut)






def etp(bot, update):
    """Send a message when the command /eth is issued."""
    etptickCall = "https://min-api.cryptocompare.com/data/price?fsym=ETP&tsyms=USD,JPY,EUR"
    etptickCallJson = requests.get(etptickCall).json()
    etptickOut = etptickCallJson 
    update.message.reply_text(etptickOut)




def etc(bot, update):
    """Send a message when the command /eth is issued."""
    etctickCall = "https://min-api.cryptocompare.com/data/price?fsym=ETC&tsyms=USD,JPY,EUR"
    etctickCallJson = requests.get(etctickCall).json()
    etctickOut = etctickCallJson 
    update.message.reply_text(etctickOut)




def omg(bot, update):
    """Send a message when the command /eth is issued."""
    omgtickCall = "https://min-api.cryptocompare.com/data/price?fsym=OMG&tsyms=USD,JPY,EUR"
    omgtickCallJson = requests.get(omgtickCall).json()
    omgtickOut = omgtickCallJson 
    update.message.reply_text(omgtickOut)



def ltc(bot, update):
    """Send a message when the command /eth is issued."""
    ltctickCall = "https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,JPY,EUR"
    ltctickCallJson = requests.get(ltctickCall).json()
    ltctickOut = ltctickCallJson 
    update.message.reply_text(ltctickOut)





def edo(bot, update):
    """Send a message when the command /eth is issued."""
    edotickCall = "https://min-api.cryptocompare.com/data/price?fsym=EDO&tsyms=USD,JPY,EUR"
    edotickCallJson = requests.get(edotickCall).json()
    edotickOut = edotickCallJson 
    update.message.reply_text(edotickOut)




def eos(bot, update):
    """Send a message when the command /eth is issued."""
    eostickCall = "https://min-api.cryptocompare.com/data/price?fsym=EOS&tsyms=USD,JPY,EUR"
    eostickCallJson = requests.get(eostickCall).json()
    eostickOut = eostickCallJson 
    update.message.reply_text(eostickOut)



def ada(bot, update):
    """Send a message when the command /eth is issued."""
    adatickCall = "https://min-api.cryptocompare.com/data/price?fsym=ADA&tsyms=USD,JPY,EUR"
    adatickCallJson = requests.get(adatickCall).json()
    adatickOut = adatickCallJson 
    update.message.reply_text(adatickOut)




def xmr(bot, update):
    """Send a message when the command /eth is issued."""
    xmrtickCall = "https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,JPY,EUR"
    xmrtickCallJson = requests.get(xmrtickCall).json()
    xmrtickOut = xmrtickCallJson 
    update.message.reply_text(xmrtickOut)





def qtum(bot, update):
    """Send a message when the command /eth is issued."""
    qtumtickCall = "https://min-api.cryptocompare.com/data/price?fsym=QTUM&tsyms=USD,JPY,EUR"
    qtumtickCallJson = requests.get(qtumtickCall).json()
    qtumtickOut = qtumtickCallJson 
    update.message.reply_text(qtumtickOut)




def xlm(bot, update):
    """Send a message when the command /eth is issued."""
    xlmtickCall = "https://min-api.cryptocompare.com/data/price?fsym=XLM&tsyms=USD,JPY,EUR"
    xlmtickCallJson = requests.get(xlmtickCall).json()
    xlmtickOut = xlmtickCallJson 
    update.message.reply_text(xlmtickOut)


def neo(bot, update):
    """Send a message when the command /eth is issued."""
    neotickCall = "https://min-api.cryptocompare.com/data/price?fsym=NEO&tsyms=USD,JPY,EUR"
    neotickCallJson = requests.get(neotickCall).json()
    neotickOut = neotickCallJson 
    update.message.reply_text(neotickOut)


def lsk(bot, update):
    """Send a message when the command /eth is issued."""
    lsktickCall = "https://min-api.cryptocompare.com/data/price?fsym=LSK&tsyms=USD,JPY,EUR"
    lsktickCallJson = requests.get(lsktickCall).json()
    lsktickOut = lsktickCallJson 
    update.message.reply_text(lsktickOut)



def dash(bot, update):
    """Send a message when the command /eth is issued."""
    dashtickCall = "https://min-api.cryptocompare.com/data/price?fsym=DASH&tsyms=USD,JPY,EUR"
    dashtickCallJson = requests.get(dashtickCall).json()
    dashtickOut = dashtickCallJson 
    update.message.reply_text(dashtickOut)



def bat(bot, update):
    """Send a message when the command /eth is issued."""
    battickCall = "https://min-api.cryptocompare.com/data/price?fsym=BAT&tsyms=USD,JPY,EUR"
    battickCallJson = requests.get(battickCall).json()
    battickOut = battickCallJson 
    update.message.reply_text(battickOut)


def nano(bot, update):
    """Send a message when the command /eth is issued."""
    nanotickCall = "https://min-api.cryptocompare.com/data/price?fsym=NANO&tsyms=USD,JPY,EUR"
    nanotickCallJson = requests.get(nanotickCall).json()
    nanotickOut = nanotickCallJson 
    update.message.reply_text(nanotickOut)



def iota(bot, update):
    """Send a message when the command /eth is issued."""
    iotatickCall = "https://min-api.cryptocompare.com/data/price?fsym=IOT&tsyms=USD,JPY,EUR"
    iotatickCallJson = requests.get(iotatickCall).json()
    iotatickOut = iotatickCallJson 
    update.message.reply_text(iotatickOut)


def zec(bot, update):
    """Send a message when the command /eth is issued."""
    zectickCall = "https://min-api.cryptocompare.com/data/price?fsym=ZEC&tsyms=USD,JPY,EUR"
    zectickCallJson = requests.get(zectickCall).json()
    zectickOut = zectickCallJson 
    update.message.reply_text(zectickOut)




def etn(bot, update):
    """Send a message when the command /eth is issued."""
    etnCall = "https://min-api.cryptocompare.com/data/price?fsym=ETN&tsyms=USD,JPY,EUR"
    etnCallJson = requests.get(etnCall).json()
    etnOut = etnCallJson 
    update.message.reply_text(etnOut)





def zrx(bot, update):
    """Send a message when the command /eth is issued."""
    zrxCall = "https://min-api.cryptocompare.com/data/price?fsym=ZRX&tsyms=USD,JPY,EUR"
    zrxCallJson = requests.get(zrxCall).json()
    zrxOut = zrxCallJson 
    update.message.reply_text(zrxOut)



def dash(bot, update):
    """Send a message when the command /eth is issued."""
    dashCall = "https://min-api.cryptocompare.com/data/price?fsym=DASH&tsyms=USD,JPY,EUR"
    dashCallJson = requests.get(dashCall).json()
    dashOut = dashCallJson 
    update.message.reply_text(dashOut)





def nuls(bot, update):
    """Send a message when the command /eth is issued."""
    nulsCall = "https://min-api.cryptocompare.com/data/price?fsym=NULS&tsyms=USD,JPY,EUR"
    nulsCallJson = requests.get(nulsCall).json()
    nulsOut = nulsCallJson 
    update.message.reply_text(nulsOut)





def iost(bot, update):
    """Send a message when the command /eth is issued."""
    iostCall = "https://min-api.cryptocompare.com/data/price?fsym=IOST&tsyms=USD,JPY,EUR"
    iostCallJson = requests.get(iostCall).json()
    iostOut = iostCallJson 
    update.message.reply_text(iostOut)



def vet(bot, update):
    """Send a message when the command /eth is issued."""
    vetCall = "https://min-api.cryptocompare.com/data/price?fsym=VET&tsyms=USD,JPY,EUR"
    vetCallJson = requests.get(vetCall).json()
    vetOut = vetCallJson 
    update.message.reply_text(vetOut)






def news(bot, update):
    randomNews = random.randint(0,30)
    """Send a message when the command /eth is issued."""
    newsCallJson = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN").json()
    newsOut = newsCallJson ['Data'][randomNews]['url']
    update.message.reply_text(newsOut)


def rules(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('1. Nothing in this forum constitutes trading advice, cryptocurrency is speculative. This is a discussion forum and no user is entitled to provide or accept advice on financial matters.'
                              + '             2. No  spamming; allow others to talk. Please make no more that 5 calls to the bot a minute'
                              + '             3. No hate speech (demonization of a particular group).'
                              + '             4. Use english primarily and NO SHOUTING.'
                              + '             5. Do not solicit your own sites or links; or use the chatroom for your own business.'
                              + '             6. Invite only: if you believe there are others who may contribute speak to one of the administrators.'
                              + '             7. If you want to excessively argue with another member, then move it to PM immediately; we do not want nor need to witness the debacle.'
                              + "             8. Be active and don't lurk, non active members will be removed."
                              + "             9. The administrators reserve the right to add or remove any user without prior warning.")




def btcrun(bot, update):
    photo = open('/tmp/photo.png', 'rb')
    update.send_photo(chat_id, photo)
    update.send_photo(chat_id, "FILEID")



def majed(bot, update):
    
    update.message.reply_text("Bitcoin Maximalist / Eminent Physics Professor / Citadel Visionary")


def zully(bot, update):
    """qdocs message"""
    update.message.reply_text("Wave Trader / Shitcoin Whale / God Given Talent")


def wacc(bot, update):
    """qdocs message"""
    update.message.reply_text("John 1:29")


def shaggy(bot, update):
    """qdocs message"""
    update.message.reply_text("Hardcore 4 Life")


def qdoc(bot, update):
    """qdocs message"""
    update.message.reply_text("Bots <3 Qdoc!")


def awg(bot, update):
    """awg message"""
    update.message.reply_text("Creator Of Chats / Collector Of Coins / Flipper Of Fiat / Master Of Money")


    





def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("685480248:AAHnEl4f2pHagojv3ueo8TlXSCE-SZNkVac")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("wall", coin, pass_args=True))
    dp.add_handler(CommandHandler("info", infoCoin, pass_args=True))
    dp.add_handler(CommandHandler("nem24", nemChange))
    dp.add_handler(CommandHandler("storm24", stormChange))
    dp.add_handler(CommandHandler("eos24", eosChange))
    dp.add_handler(CommandHandler("btc24", btcChange))
    dp.add_handler(CommandHandler("etc24", etcChange))
    dp.add_handler(CommandHandler("eth24", ethChange))
    dp.add_handler(CommandHandler("bnb24", bnbChange))
    dp.add_handler(CommandHandler("etp24", etpChange))
    dp.add_handler(CommandHandler("bat24", batChange))
    dp.add_handler(CommandHandler("ltc24", ltcChange))
    dp.add_handler(CommandHandler("gnt24", gntChange))
    dp.add_handler(CommandHandler("ont24", ontChange))
    dp.add_handler(CommandHandler("neo24", neoChange))
    dp.add_handler(CommandHandler("dcr24", dcrChange))
    dp.add_handler(CommandHandler("trx24", trxChange))
    dp.add_handler(CommandHandler("zrx24", zrxChange))
    dp.add_handler(CommandHandler("vet24", vetChange))
    dp.add_handler(CommandHandler("iota24", iotaChange))
    dp.add_handler(CommandHandler("edo24", edoChange))
    dp.add_handler(CommandHandler("ada24", adaChange))
    dp.add_handler(CommandHandler("btccap", btcCap))
    dp.add_handler(CommandHandler("ethcap", ethCap))



    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("btc", btc))
    dp.add_handler(CommandHandler("eth", eth))
    dp.add_handler(CommandHandler("bnb", bnb))
    dp.add_handler(CommandHandler("etp", etp))
    dp.add_handler(CommandHandler("etc", etc))
    dp.add_handler(CommandHandler("omg", omg))
    dp.add_handler(CommandHandler("ltc", ltc))
    dp.add_handler(CommandHandler("edo", edo))
    dp.add_handler(CommandHandler("eos", eos))
    dp.add_handler(CommandHandler("ada", ada))
    dp.add_handler(CommandHandler("xmr", xmr))
    dp.add_handler(CommandHandler("xlm", xlm))
    dp.add_handler(CommandHandler("lsk", lsk))
    dp.add_handler(CommandHandler("bat", bat))
    dp.add_handler(CommandHandler("nano", nano))
    dp.add_handler(CommandHandler("iota", iota))
    dp.add_handler(CommandHandler("zec", zec))
    dp.add_handler(CommandHandler("etn", etn))
    dp.add_handler(CommandHandler("zrx", zrx))
    dp.add_handler(CommandHandler("nuls", nuls))
    dp.add_handler(CommandHandler("iost", iost))
    dp.add_handler(CommandHandler("vet", vet))
    dp.add_handler(CommandHandler("qtum", qtum))
    dp.add_handler(CommandHandler("dash", dash))
    dp.add_handler(CommandHandler("xrp", xrp))
    dp.add_handler(CommandHandler("nem", nemChange))
    dp.add_handler(CommandHandler("news", news))



    dp.add_handler(CommandHandler("qdoc", qdoc))
    dp.add_handler(CommandHandler("awg", awg))
    dp.add_handler(CommandHandler("majed", majed))
    dp.add_handler(CommandHandler("zully", zully))
    dp.add_handler(CommandHandler("wacc", wacc))
    dp.add_handler(CommandHandler("shaggy", shaggy))




    # on noncommand i.e message - echo the message on Telegram


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
