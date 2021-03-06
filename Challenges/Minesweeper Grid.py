from test import Test
       
def num_grid(lst):
    ret = lst
    rSize = len(lst)
    cSize = len(lst[0])
    for i in range(rSize):
        for j in range(cSize):
            cnt = 0
            if lst[i][j] == '#':
                continue
            #RIGHT SIDE
            if j+1 < cSize and lst[i][j+1] == '#':
                cnt+=1
            if j+1 < cSize and i+1 < rSize and lst[i+1][j+1] == '#':
                cnt+=1
            if j+1 < cSize and i-1 >= 0 and lst[i-1][j+1] == '#':
                cnt+=1
            #LEFT SIDE
            if j-1 >= 0 and lst[i][j-1] == '#':
                cnt+=1
            if j-1 >= 0 and i+1 < rSize and lst[i+1][j-1] == '#':
                cnt+=1
            if j-1 >= 0 and i-1 >= 0 and lst[i-1][j-1] == '#':
                cnt+=1
            #TOP AND BOTTOM
            if i+1 < rSize and lst[i+1][j] == '#':
                cnt+=1
            if i-1 >= 0 and lst[i-1][j] == '#':
                cnt+=1
            ret[i][j] = str(cnt)
    return ret
                
print(num_grid([
['-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-']
]))
Test.assert_equals(num_grid([
['-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '-', '-', '-', '-'],
['-', '-', '-', '-', '-']
]), [
['0', '0', '0', '0', '0'],
['0', '1', '1', '1', '0'],
['0', '1', '#', '1', '0'],
['0', '1', '1', '1', '0'],
['0', '0', '0', '0', '0']
])

Test.assert_equals(num_grid([
['-', '-', '-', '-', '#'],
['-', '-', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '-', '-', '-', '-'],
['#', '-', '-', '-', '-']
]), [
['0', '0', '0', '1', '#'],
['0', '1', '1', '2', '1'],
['0', '1', '#', '1', '0'],
['1', '2', '1', '1', '0'],
['#', '1', '0', '0', '0']
])

Test.assert_equals(num_grid([
['-', '-', '-', '#', '#'],
['-', '#', '-', '-', '-'],
['-', '-', '#', '-', '-'],
['-', '#', '#', '-', '-'],
['-', '-', '-', '-', '-']
]), [
['1', '1', '2', '#', '#'],
['1', '#', '3', '3', '2'],
['2', '4', '#', '2', '0'],
['1', '#', '#', '2', '0'],
['1', '2', '2', '1', '0']
])