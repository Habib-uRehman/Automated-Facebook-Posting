{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1f0341c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "9eeb2cee",
   "metadata": {},
   "outputs": [],
   "source": [
    "msg = \"That which does not kill us makes us stronger. – Friedrich Nietzsche\"\n",
    "token = 'EAANBluq9BjABAOichFwNM4AyQQDIigMU5trcgB6tz3pZCAt5ZCv3Qc1wZB55OOMJGZB206RHVQIDxZAVcDIuP1QZAsbtp9a0yEU90S0Y4yBPZBZBGbNNcjQACpmZBixVfUO5NahtvE24y13uaPqxoVHpDJRZBauzGlVedGCDpH65M6o2Vtolqcxc1rSFrfeUoaeiBYn7G1rWbfdAZDZD'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "5796a46c",
   "metadata": {},
   "outputs": [],
   "source": [
    "post_url = \"https://graph.facebook.com/444272846392416/feed\"\n",
    "payload = {\n",
    "    'message':msg,\n",
    "    'access_token':token\n",
    "    \n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "9b9938e6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'{\"id\":\"444272846392416_410357480660211\"}'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re = requests.post(post_url, data=payload)\n",
    "re.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "8ba3435e",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'GET http://quotes.rest/quote/random.json'\n",
    "key = 'd937f87084f13718cb163dc40ab256dd'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "6445742c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ALove is composed of a single soul inhabiting two bodies.rLove is composed of a single soul inhabiting two bodies.iLove is composed of a single soul inhabiting two bodies.sLove is composed of a single soul inhabiting two bodies.tLove is composed of a single soul inhabiting two bodies.oLove is composed of a single soul inhabiting two bodies.tLove is composed of a single soul inhabiting two bodies.lLove is composed of a single soul inhabiting two bodies.e\n"
     ]
    }
   ],
   "source": [
    "url = 'https://favqs.com/api/qotd'\n",
    "req = requests.get(url)\n",
    "d = req.json()\n",
    "quote = d['quote']['body']\n",
    "author = d['quote']['author']\n",
    "msg = quote+author\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad616b1c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9750718",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
