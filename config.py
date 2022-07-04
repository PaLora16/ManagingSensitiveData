class pavels_config():
    _config = {
        "drink":
            {
                "non_alcoholic": ("herbal_tea", "pure_water"),
                "booze": {
                    "scotch": ("gAAAAABhkPaAtCc4N284mkn0T9vIK9IY2YrLv7ktuPLMwunPqpRcrZKwbDOvRcCS78_87wzHqALflpFMaGhpnfJtYesG6HLzeg==")
                }
            }
    }


def get_scotch(self) -> str:
    return self._config["drink"]["booze"]["scotch"]
