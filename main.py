# =SUM(INDIRECT("keys!B"&MATCH(B2, keys!A1:A9, 0)), INDIRECT("keys!C"&MATCH(C2, keys!A1:A9, 0)), INDIRECT("keys!D"&MATCH(D2, keys!A1:A9, 0)), INDIRECT("keys!E"&MATCH(E2, keys!A1:A9, 0)), INDIRECT("keys!F"&MATCH(F2, keys!A1:A9, 0)))


for i in range(2, 45, 1):
    print(f'=SUM(INDIRECT("keys!B"&MATCH(B{i}, keys!A1:A9, 0)), INDIRECT('
          f'"keys!C"&MATCH(C{i}, keys!A1:A9, 0)), INDIRECT("keys!D"&MATCH(D'
          f'{i}, '
          f'keys!A1:A9, 0)), INDIRECT("keys!E"&MATCH(E{i}, keys!A1:A9, 0)), '
          f'INDIRECT("keys!F"&MATCH(F{i}, keys!A1:A9, 0)))')