event.deep_walk("source", "ip", (("network")), default="no-ip")
            #  ^ punctuation.arg_open
            #   ^ string.function_arg
            #             ^ string.function_arg
                            #     ^ string
                            #                  ^ keyword_arg
                                            #          ^ string.keyword_arg
                                            #                 ^ punctuation.arg_close
event.deep_get("source", "ip", "network")
    # ^ function.method
            # ^ punctuation.arg_open
            #  ^ string.function_arg
            #            ^ string.function_arg
            #                   ^ string.function_arg
            #                           ^ punctuation.arg_close
event.deep_get(retries=3)
              #^ keyword_arg