for data in exported_data:
            c = 0
            for item in data:
                if 'Total' in data:
                    if item == 'Total':
                        worksheet.write(r, c, item, style_head23)
                    elif item or item == 0.0:
                        worksheet.write(r, c, item, style_head23)

                else:
                    worksheet.write(r, c, item, decimal_style)

                c += 1
            r += 1

        if r > 1:
            if self.report_type == 'portfolio':
                if self.type == "detailed_report":
                    worksheet.write(r, 0, "Total", bold)
                    worksheet.write(r, 27, xlwt.Formula(
                    "SUM(AB8:AB%d)" % (r)), decimal_style1)
                    worksheet.write(r, 28, xlwt.Formula(
                    "SUM(AC8:AC%d)" % (r)), decimal_style1)
                    worksheet.write(r, 29, xlwt.Formula(
                    "SUM(AD8:AD%d)" % (r)), decimal_style1)
                    worksheet.write(r, 30, xlwt.Formula(
                    "SUM(AE8:AE%d)" % (r)), decimal_style1)
                    worksheet.write(r, 31, xlwt.Formula(
                    "SUM(AF8:AF%d)" % (r)), decimal_style1)

                    worksheet.write(r, 37, xlwt.Formula(
                    "SUM(AL8:AL%d)" % (r)), decimal_style1)
                    worksheet.write(r, 38, xlwt.Formula(
                    "SUM(AM8:AM%d)" % (r)), decimal_style1)

                    worksheet.write(r, 39, xlwt.Formula(
                    "SUM(AN8:AN%d)" % (r)), decimal_style1)
                    worksheet.write(r, 40, xlwt.Formula(
                    "SUM(AO8:AO%d)" % (r)), decimal_style1)
                    worksheet.write(r, 41, xlwt.Formula(
                    "SUM(AP8:AP%d)" % (r)), decimal_style1)
                    worksheet.write(r, 42, xlwt.Formula(
                    "SUM(AQ8:AQ%d)" % (r)), decimal_style1)
                    worksheet.write(r, 43, xlwt.Formula(
                    "SUM(AR8:AR%d)" % (r)), decimal_style1)
                    worksheet.write(r, 44, xlwt.Formula(
                    "SUM(AS8:AS%d)" % (r)), decimal_style1)
                    worksheet.write(r, 45, xlwt.Formula(
                    "SUM(AT8:AT%d)" % (r)), decimal_style1)
                    worksheet.write(r, 46, xlwt.Formula(
                    "SUM(AU8:AU%d)" % (r)), decimal_style1)
                    worksheet.write(r, 47, xlwt.Formula(
                    "SUM(AV8:AV%d)" % (r)), decimal_style1)
                    worksheet.write(r, 48, xlwt.Formula(
                    "SUM(AW8:AW%d)" % (r)), decimal_style1)
                    worksheet.write(r, 49, xlwt.Formula(
                    "SUM(AX8:AX%d)" % (r)), decimal_style1)
                    worksheet.write(r, 50, xlwt.Formula(
                    "SUM(AY8:AY%d)" % (r)), decimal_style1)
                    worksheet.write(r, 51, xlwt.Formula(
                    "SUM(AZ8:AZ%d)" % (r)), decimal_style1)
                    worksheet.write(r, 52, xlwt.Formula(
                    "SUM(BA8:BA%d)" % (r)), decimal_style1)
                    worksheet.write(r, 53, xlwt.Formula(
                    "SUM(BB8:BB%d)" % (r)), decimal_style1)
                    worksheet.write(r, 54, xlwt.Formula(
                    "SUM(BC8:BC%d)" % (r)), decimal_style1)
                    worksheet.write(r, 55, xlwt.Formula(
                    "SUM(BD8:BD%d)" % (r)), decimal_style1)
                    worksheet.write(r, 56, xlwt.Formula(
                    "SUM(BE8:BE%d)" % (r)), decimal_style1)
                    worksheet.write(r, 57, xlwt.Formula(
                    "SUM(BF8:BF%d)" % (r)), decimal_style1)
                    worksheet.write(r, 58, xlwt.Formula(
                    "SUM(BG8:BG%d)" % (r)), decimal_style1)
                    worksheet.write(r, 59, xlwt.Formula(
                    "SUM(BH8:BH%d)" % (r)), decimal_style1)
                    worksheet.write(r, 60, xlwt.Formula(
                    "SUM(BI8:BI%d)" % (r)), decimal_style1)
                    worksheet.write(r, 61, xlwt.Formula(
                    "SUM(BJ8:BJ%d)" % (r)), decimal_style1)

                    worksheet.write(r, 62, xlwt.Formula(
                    "SUM(BK8:BK%d)" % (r)), decimal_style1)
                    worksheet.write(r, 63, xlwt.Formula(
                    "SUM(BL8:BL%d)" % (r)), decimal_style1)
                    worksheet.write(r, 64, xlwt.Formula(
                    "SUM(BM8:BM%d)" % (r)), decimal_style1)
                    worksheet.write(r, 65, xlwt.Formula(
                    "SUM(BN8:BN%d)" % (r)), decimal_style1)
                    worksheet.write(r, 66, xlwt.Formula(
                    "SUM(BO8:BO%d)" % (r)), decimal_style1)
                    worksheet.write(r, 67, xlwt.Formula(
                    "SUM(BP8:BP%d)" % (r)), decimal_style1)
                    worksheet.write(r, 68, xlwt.Formula(
                    "SUM(BQ8:BQ%d)" % (r)), decimal_style1)
                    worksheet.write(r, 69, xlwt.Formula(
                    "SUM(BR8:BR%d)" % (r)), decimal_style1)
                    worksheet.write(r, 70, xlwt.Formula(
                    "SUM(BS8:BS%d)" % (r)), decimal_style1)
                    worksheet.write(r, 71, xlwt.Formula(
                    "SUM(BT8:BT%d)" % (r)), decimal_style1)
                    worksheet.write(r, 72, xlwt.Formula(
                    "SUM(BU8:BU%d)" % (r)), decimal_style1)
                    worksheet.write(r, 73, xlwt.Formula(
                    "SUM(BV8:BV%d)" % (r)), decimal_style1)
                    worksheet.write(r, 74, xlwt.Formula(
                    "SUM(BW8:BW%d)" % (r)), decimal_style1)
                    worksheet.write(r, 75, xlwt.Formula(
                    "SUM(BX8:BX%d)" % (r)), decimal_style1)
                    worksheet.write(r, 76, xlwt.Formula(
                    "SUM(BY8:BY%d)" % (r)), decimal_style1)
                    worksheet.write(r, 77, xlwt.Formula(
                    "SUM(BZ8:BZ%d)" % (r)), decimal_style1)
                    worksheet.write(r, 78, xlwt.Formula(
                    "SUM(CA8:CA%d)" % (r)), decimal_style1)
                    worksheet.write(r, 79, xlwt.Formula(
                    "SUM(CB8:CB%d)" % (r)), decimal_style1)
                    worksheet.write(r, 80, xlwt.Formula(
                    "SUM(CC8:CC%d)" % (r)), decimal_style1)
                    worksheet.write(r, 81, xlwt.Formula(
                    "SUM(CD8:CD%d)" % (r)), decimal_style1)
                    worksheet.write(r, 82, xlwt.Formula(
                    "SUM(CE8:CE%d)" % (r)), decimal_style1)
                    worksheet.write(r, 83, xlwt.Formula(
                    "SUM(CF8:CF%d)" % (r)), decimal_style1)
                    worksheet.write(r, 84, xlwt.Formula(
                    "SUM(CG8:CG%d)" % (r)), decimal_style1)