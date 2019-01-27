import random
from collections import namedtuple

import requests
from bs4 import BeautifulSoup
from errbot import BotPlugin, arg_botcmd


ShopInfo = namedtuple('ShopInfo', ('name', 'url'))


class JpFoods(BotPlugin):
    def get_configuration_template(self):
        return {
            'RWS_API_KEY': '000011112222',
            'RWS_AREA_CODE': 'XX00',
            'GNAVI_API_KEY': '000011112222',
            'GNAVI_AREA_CODE': 'AREAS00000',
        }

    @arg_botcmd('keyword', type=str)
    def jp_foods_search(self, msg, keyword):
        """Hotpepper, ぐるなびから、周辺のお店情報を検索します
        """
        shop_list = []
        shop_list += self._search_by_rws(keyword)
        shop_list += self._search_by_gnavi(keyword)
        if len(shop_list) == 0:
            return '検索に引っかかりませんでした'
        return '\n'.join([f"- {s.name} {s.url}" for s in shop_list])

    @arg_botcmd('keyword', type=str)
    @arg_botcmd('-n', '--num', dest='num', type=int, default=3)
    def jp_foods_choice(self, msg, keyword, num=3):
        shop_list = []
        shop_list += self._search_by_rws(keyword)
        shop_list += self._search_by_gnavi(keyword)
        if len(shop_list) == 0:
            return 'キーワード検索に引っかかりませんでした'
        return 'このあたりはどうでしょう？\n' + \
            '\n'.join([
                f"- {s.name} {s.url}" for s in random.sample(shop_list, num)
            ])

    def _search_by_rws(self, keyword):
        """周辺のホットペッパー掲載サイトをキーワード検索します
        """
        api_key = self.config.get('RWS_API_KEY', False)
        if not api_key:
            return []
        area_code = self.config.get('RWS_AREA_CODE', False)
        if not area_code:
            return []
        # Fetch from RWS の小マスターAPIを利用（エリア:Y005
        url = f"http://webservice.recruit.co.jp/hotpepper/gourmet/v1/" \
            f"?key={api_key}&small_area={area_code}&keyword={keyword}"
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        shop_list = []
        for s in soup.find_all('shop'):
            shop_list.append(
                ShopInfo(s.find('name').string, s.urls.pc.string))
        return shop_list

    def _search_by_gnavi(self, keyword):
        api_key = self.config.get('GNAVI_API_KEY', False)
        if not api_key:
            return []
        # 晴海
        area_code = self.config.get('GNAVI_AREA_CODE', False)
        if not area_code:
            return []
        url = f"https://api.gnavi.co.jp/RestSearchAPI/v3/"\
            f"?keyid={api_key}&areacode_s={area_code}&freeword={keyword}"
        resp = requests.get(url)
        data = resp.json()
        shop_list = []
        for s in data.get('rest', []):
            shop_list.append(
                ShopInfo(s['name'], s['url']))
        return shop_list
