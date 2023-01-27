class UnifiedList:
    def __init__(self, BoM, Disti):
        self.BoM = BoM
        self.Disti = Disti

    def compare_lists(self):
        unified_list = []
        for part in self.BoM:
            if part in self.Disti:
                if self.BoM[part] < self.Disti[part]:
                    disti_qty = self.BoM[part]
                    self.Disti[part] -= disti_qty
                    unified_list.append({"bom_pn": part, "bom_qty": self.BoM[part], "dsti_pn": part, "dsti_qty": disti_qty, "error_flag": False})
                else:
                    unified_list.append({"bom_pn": part, "bom_qty": self.BoM[part], "dsti_pn": part, "dsti_qty": self.Disti[part], "error_flag": False})
                    self.Disti[part] = 0
            else:
                unified_list.append({"bom_pn": part, "bom_qty": self.BoM[part], "dsti_pn": None, "dsti_qty": None, "error_flag": True})

        return unified_list
