import random
from faker import Faker

fake = Faker(['bg_BG',   'cs_CZ', 'da_DK', 'de_DE', 'en_US', 
              'es_ES', 'fi_FI', 'fr_FR',  'it_IT',  
              'nl_NL', 'pl_PL', 'pt_BR'])
              
            #   'ro_RO', 'ru_RU', 'hr_HR', 'sk_SK', 
            #   'sq_AL', 'sv_SE', 'th_TH', 'tr_TR', 'ur_PK', 'id_ID', 'uk_UA', 'be_BY', 'sl_SI',
            #   'et_EE', 'lv_LV', 'lt_LT', 'tg_Cyrl_TJ', 'fa_IR', 'vi_VN', 'hy_AM', 'az_Latn_AZ', 
            #   'eu_ES', 'wen_DE', 'mk_MK', 'st_ZA', 'ts_ZA', 'tn_ZA', 'ven_ZA', 'xh_ZA', 'zu_ZA', 
            #   'af_ZA', 'ka_GE', 'fo_FO', 'hi_IN', 'mt_MT', 'se_NO', 'gd_GB', 'ms_MY', 'kk_KZ', 
            #   'ky_KG', 'sw_KE', 'tk_TM', 'uz_Latn_UZ', 'tt_RU', 'bn_IN', 'pa_IN', 'gu_IN', 'or_IN', 
            #   'ta_IN', 'te_IN', 'kn_IN', 'ml_IN', 'as_IN', 'mr_IN', 'sa_IN', 'mn_MN', 'bo_CN', 
            #   'cy_GB', 'km_KH', 'lo_LA', 'my_MM', 'gl_ES', 'kok_IN', 'sd_IN', 'syr_SY', 'si_LK', 
            #   'chr_US', 'iu_Cans_CA', 'am_ET', 'ks_Arab_IN', 'ne_NP', 'fy_NL', 'ps_AF', 'fil_PH', 
            #   'dv_MV', 'bin_NG', 'fuv_NG', 'ha_Latn_NG', 'ibb_NG', 'yo_NG', 'quz_BO', 'nso_ZA', 
            #   'ig_NG', 'kr_NG', 'gaz_ET', 'ti_ER', 'gn_PY', 'haw_US', 'so_SO', 'ii_CN', 'pap_AN', 
            #   'ug_Arab_CN', 'mi_NZ', 'ar_IQ', 'zh_CN', 'de_CH', 'en_GB', 'es_MX', 'fr_BE', 'it_CH', 
            #   'nl_BE', 'nn_NO', 'pt_PT', 'ro_MD', 'ru_MD', 'sr_Latn_CS', 'sv_FI', 'ur_IN', 
            #   'az_Cyrl_AZ', 'ga_IE', 'ms_BN', 'uz_Cyrl_UZ', 'bn_BD', 'pa_PK', 'mn_Mong_CN', 'bo_BT', 
            #   'sd_PK', 'tzm_Latn_DZ', 'ks_Deva_IN', 'ne_IN', 'quz_EC', 'ti_ET', 'ar_EG', 'zh_HK', 'de_AT', 
            #   'en_AU', 'es_ES', 'fr_CA', 'sr_Cyrl_CS', 'quz_PE', 'ar_LY', 'zh_SG', 'de_LU', 'en_CA', 'es_GT', 
            #   'fr_CH', 'hr_BA', 'ar_DZ', 'zh_MO', 'de_LI', 'en_NZ', 'es_CR', 'fr_LU', 'bs_Latn_BA', 'ar_MO', 
            #   'en_IE', 'es_PA', 'fr_MC', 'ar_TN', 'en_ZA', 'es_DO', 'fr_029', 'ar_OM', 'en_JM', 'es_VE', 
            #   'fr_RE', 'ar_YE', 'en_029', 'es_CO', 'fr_CG', 'ar_SY', 'en_BZ', 'es_PE', 'fr_SN', 'ar_JO', 
            #   'en_TT', 'es_AR', 'fr_CM', 'ar_LB', 'en_ZW', 'es_EC', 'fr_CI', 'ar_KW', 'en_PH', 'es_CL', 
            #   'fr_ML', 'ar_AE', 'en_ID', 'es_UY', 'fr_MA', 'ar_BH', 'en_HK', 'es_PY', 'fr_HT', 'ar_QA', 
            #   'en_IN', 'es_BO', 'en_MY', 'es_SV', 'en_SG', 'es_HN', 'es_NI', 'es_PR', 'es_US', 'es_419', 
            #   'fr_015'])
possible_names = set()

while len(possible_names) < 5900:
    name = fake.name().split()[0]
    if '-' in name:
        name = name.split('-')[0]
    
    if name not in possible_names:
        possible_names.add(name)

connections = set()
possible_names = list(possible_names)

while len(connections) < 1000000:
    person_1 = random.choice(possible_names)
    person_2 = random.choice(possible_names)

    if person_1 == person_2:
        continue

    if (person_1, person_2) in connections or (person_2, person_1) in connections:
        continue
    
    connections.add((person_1, person_2))


from collections import defaultdict
answer = defaultdict(lambda: 0)

with open('src/io/input/friends.txt', 'w') as file:
    for name1, name2 in connections:
        print(f'{name1}, {name2}', file=file)
        answer[name1] += 1

with open('src/io/input/friends_answer.txt', 'w') as file:
    for name1, no_friends in answer.items():
        print(f'{name1} {no_friends}', file=file)

# friends = set()
# repeat_a = []
# repeat_b = []


# for _ in range(MAX):
#   name1 = fake.name()
#   name2 = fake.name()
#   connection = (name1.split()[0], name2.split()[0])

#   if connection not in friends:
#     friends.add(connection)
#     a, b = connection
#     print(f"{a}, {b}")
#     repeat_a.append(a)
#     repeat_b.append(b)
#   else:
#     continue
