# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> with_test
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/4/29 12:16 下午
# @Desc   ：
# ==================================================
import re
import logging

import json
import time

import GlobalParameters
import os


def get_test():
    try:
        with open(GlobalParameters.test_file, encoding="utf-8", mode="w") as opened_file:
            opened_file.write("hello")
    except FileNotFoundError:
        os.mknod(GlobalParameters.test_file)


if __name__ == '__main__':
    # get_test()
    context = []
    context1 = ""
    with open("../data/test.txt", encoding="utf-8") as f:
        # for x in f:
        #     context.append(x.replace("\n",""))
        context1 = f.read()
    dict = {"str": context1}
    json = json.dumps(dict)
    print(json)
    # str1 = "[]"
    # str = "['1', '16', '17', '18', '19', '20', '21', '22', '23', '24', '31', '42', '43', '45', '46', '47', '48', '127', '172', '235', '236', '237', '250', '251', '252', '253', '254', '255', '256', '257', '258', '259', '260', '261', '262', '263', '264', '265', '266', '267', '268', '269', '270', '271', '272', '273', '274', '275', '276', '277', '278', '279', '280', '281', '282', '283', '284', '285', '286', '287', '288', '289', '291', '292', '293', '294', '295', '297', '298', '299', '300', '340', '384', '385', '387', '388', '389', '393', '451', '453', '455', '456', '457', '461', '481', '482', '483', '487', '493', '512', '513', '516', '517', '522', '523', '531', '608', '640', '641', '642', '643', '644', '645', '649', '655', '768', '769', '770', '771', '772', '773', '899', '902', '903', '904', '905', '910', '911', '917', '919', '920', '921', '925', '1000', '1001', '1103', '1105', '1301', '1302', '1303', '1304', '1305', '1306', '1307', '1308', '1309', '1310', '1311', '1312', '1313', '1314', '1315', '1316', '1317', '1318', '1319', '1320', '1321', '1322', '1323', '1324', '1325', '1326', '1327', '1328', '1329', '1330', '1331', '1332', '1333', '1334', '1335', '1336', '1337', '1338', '1339', '1340', '1341', '1342', '1343', '1344', '1345', '1346', '1347', '1348', '1349', '1350', '1351', '1352', '1353', '1354', '1355', '1356', '1357', '1358', '1359', '1360', '1361', '1362', '1363', '1364', '1366', '1367', '1368', '1369', '1370', '1371', '1372', '1373', '1374', '1375', '1376', '1377', '1379', '1380', '1381', '1382', '1383', '1384', '1385', '1386', '1387', '1498', '1499', '1500', '2000', '3931', '3936', '3937', '3939', '3942', '3943', '3944', '3945', '3946', '3947', '3948', '3949', '3950', '3951', '3952', '3953', '3954', '3955', '3956', '3957', '3958', '3959', '3961', '3962', '3963', '3964', '3965', '3967']"
    # text = str.replace("[", " ").replace("]", " ").replace('\'', '').strip()
    # lis_text = [x for x in text]
    # print(text)
    # now_milli_time = int(time.time() * 1000)
    # print(now_milli_time)
    # dict_list = {}
    # dict_list["vlanId"] = text
    # json = json.dumps(dict_list)
    # print(json)
    lis1 = [1, 3, 5]
    lis2 = [3, 5, 7, 8]
    lis1.extend(lis2)
    lis1 = list(set(lis1))
    print(lis1)
    lis3 = []
    print(lis3.__len__())
    str1 = "[]"
    lis4 = []
    text = str1.replace("[", " ").replace("]", " ").replace('\'', '').strip().split(",")
    for x in text:
        if x:
            lis3.append(x)
    print(lis4.__len__(),lis4)
    logging.info("asdasdasd")