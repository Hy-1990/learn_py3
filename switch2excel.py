# -*- coding: UTF-8 -*-
# =================================================
# @Project -> File   ：utils -> switch2excel
# @IDE    ：PyCharm
# @Author ：至尊宝
# @Date   ：2020/4/27 3:39 下午
# @Desc   ：
# ==================================================
import openpyxl
import GlobalParameters


class er_cell:
    line_name = ""
    source_name = ""
    targer_name = ""
    source_port = ""
    targer_port = ""
    template_name = "关系模板"
    port_id = ""

    def set_line_name(self, value):
        self.line_name = value

    def set_source_name(self, value):
        self.source_name = value

    def set_target_name(self, value):
        self.targer_name = value

    def set_source_port(self, value):
        self.source_port = value

    def set_targer_port(self, value):
        self.targer_port = value

    def set_port_id(self, value):
        self.port_id = value

    def __str__(self) -> str:
        return "{" + "line_name:" + self.line_name + "," + "source_name:" + self.source_name + \
               "," + "targer_name:" + self.targer_name + "," + "source_port:" + self.source_port + \
               "," + "targer_port:" + self.targer_port + "," + "template_name:" + self.template_name + \
               "," + "port_id:" + self.port_id + "}"


def switch2excel(data, file):
    host = open(GlobalParameters.host_file, encoding="utf-8")
    dict_host = {}
    dict_ip = {}
    for sen_host in host:
        if sen_host != "" and sen_host.split().__len__() > 0:
            if sen_host.split()[0] not in dict_host:
                dict_host[sen_host.split()[0]] = sen_host.split()[1]
            if sen_host.split()[1] not in dict_ip:
                dict_ip[sen_host.split()[1]] = sen_host.split()[0]

    print(str(dict_host))
    print(str(dict_ip))

    f = open(data, encoding="utf-8")
    sen_list = []
    count = 0;
    for sentence in f:
        if sentence:
            sen_list.append(sentence.strip())
            if len(sentence.strip().split(",")) == 1:
                count = count + 1
    print(count)
    print(len(sen_list))
    print(sen_list)

    line_id = 0
    er_cells = []
    source_name = ""
    for i in range(len(sen_list)):
        sen_spl = sen_list[i].split(",")
        if len(sen_spl) == 1:
            source_name = sen_spl[0].split()[1].strip()
        elif len(sen_spl) == 7:
            x = er_cell()
            if source_name in dict_ip:
                x.set_source_name(dict_ip[source_name])
            else:
                x.set_source_name(source_name)

            if sen_spl[0] is not None:
                x.set_port_id(sen_spl[0].strip())

            if sen_spl[1] is not None:
                x.set_source_port(sen_spl[1].strip())

            if sen_spl[3] is not None:
                # if sen_spl[3].strip() in dict_host:
                #     x.set_target_name(dict_host[sen_spl[3].strip()])
                # else:
                x.set_target_name(sen_spl[3].strip())

            if sen_spl[6] is not None:
                x.set_targer_port(sen_spl[6].strip())

            x.set_line_name("line" + str(line_id))
            er_cells.append(x)
            line_id = line_id + 1
    excel_file = openpyxl.Workbook()
    sheet = excel_file.create_sheet(title="lines")
    for i in range(len(er_cells) + 1):
        if i == 0:
            sheet.append(["lineName", "sourceName", "targetName", "sourcePort",
                          "targetPort", "web_color", "web_title", "web_shape",
                          "web_offset", "web_line_width", "web_source_anchor",
                          "web_target_anchor", "web_end_arrow", "templateName", "portId"])
        else:
            sheet.append([er_cells[i - 1].line_name, er_cells[i - 1].source_name, er_cells[i - 1].targer_name,
                          er_cells[i - 1].source_port, er_cells[i - 1].targer_port, "", "",
                          "", "", "", "", "", "", er_cells[i - 1].template_name, er_cells[i - 1].port_id])
    excel_file.save(file)


if __name__ == '__main__':
    switch2excel(GlobalParameters.switch_file, GlobalParameters.excel_file)
