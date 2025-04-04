from requests import Request, Session
import json

#websites change hence unless u change the code, the code may become outdated
headers___={

"Cookie":"tt_chain_token=Q2ZMBexUMOK/5iLPJlGKpQ==; tiktok_webapp_theme_source=auto; tiktok_webapp_theme=dark; odin_tt=4336ea384e0452fd853471bfc5d09ce27eb94d57d8d8a040cd3d8edcc26276e932ee0a630cfa27304ed7d671490b2561658f743274d26e5491c697f1ee02faf29d51b5dcc3c4981641c8612f4b287564; delay_guest_mode_vid=5; tt_csrf_token=wmpooZKW-VgCLqjGGpUDziCN8FEL0wSWXA5I; ttwid=1%7CpXQzWrgDyWPhbnn5ivklq3_ddl7wiv1lKAosl3uAeIM%7C1743588928%7C35c8d9cb6ae4f0aef167e9d5107c4f9dc78d5129691d86b3c43f0abeebf36708; perf_feed_cache={%22expireTimestamp%22:1743760800000%2C%22itemIds%22:[%227480119139282046230%22%2C%227481638832530672903%22]}; msToken=9kdc4-mwwUP0zNkVh7ZwbxG6LOeMZgkRUH86VxCMift6S1hYlQEJiQgkYu36Pfy20d3oMaVoP0xLRTlOtEsPIyFZmwbVIeBU0ww_BNLznKxee3e3lweUlI0vLZg3YtUHJ8xbCaVvPH9M-ysYgZJ-VFIi; msToken=-0Lt9NZO4yEjVslcRTsCezVsR9vUAFMM54MUiZAr30F40tPa8mfFqTLSSJHplS4hBdNeHVuEsnIVuNxWICe8IHB4KMXvxMxAevqRJarf34w-j47nnDgycI2qSFFQohO5zdwQpAjimeFOqYseR6BK0xbp",
"Sec-Ch-Ua": '"Not:A-Brand";v="24", "Chromium";v="134"',
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Ch-Ua-Platform": '"Windows"',
"Accept-Language": "en-US,en;q=0.9",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Priority": "u=0, i"


}
#a more simpler way would be to use request.get but i didnt to enable more flexibility, just in case
s = Session()
searchquery="hjalderkhilji"

req = Request('GET', f"https://tiktok.com/api/search/general/preview/?WebIdLastTime=1743030249&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F134.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&data_collection_enabled=false&device_id=7486257885664626194&device_platform=web_pc&focus_state=true&from_page=fyp&history_len=3&is_fullscreen=false&is_page_visible=true&keyword={searchquery}&odinId=7486257740722226183&os=windows&priority_region=&referer=&region=PK&screen_height=900&screen_width=1600&tz_name=Asia%2FKarachi&user_is_login=false&webcast_language=en")
req = req.prepare()

response = s.send(req, timeout=5)
print(json.loads(response.content))
#if "rich_sug_avatar_uri" in (json.load(response)["sug_list"])[search_result_number]["extra_info"] then its a account result
#else its a normal search result
all_non_account_results=[]
for individual_search_results in (json.loads(response.content))["sug_list"]:
    if "rich_sug_avatar_uri" in individual_search_results["extra_info"]:
        break
    else:
        search_result_name=individual_search_results["content"]
        all_non_account_results.append(search_result_name)
        #all_non_account_results+=individual_search_results["content"] dont use this line cuz it will treat as a list 
        #containing charactors instead of a string, use the line above instead!!!
        req = Request('GET', "https://www.tiktok.com/search")
        paremeters_of_search= {"q":search_result_name}
        req = req.prepare()
        req.headers=headers___
        response = s.send(req, timeout=5)
        print(response.content)

print('\n\n\n\n\n')
print(all_non_account_results)


