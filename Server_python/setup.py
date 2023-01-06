#NOTE: file nay dung de khai bao cac vat the can duoc phat hien khi su dung,
# neu muon chinh sua them bot cac vat the thi chinh sua trong file nay
#
#

import os

# Khai bao
LABEL_MAP_NAME = 'label_map.pbtxt'
files = {
	'LABELMAP': os.path.join(LABEL_MAP_NAME)
}
labels = [{'name': 'toc_do_20', 'id': 1}, {'name': 'toc_do_80', 'id': 2 }, {'name': 'dung_xe', 'id': 3}, 
	{'name': 'duong_cam', 'id': 4}, {'name': 'cb_nguoi_di_bo', 'id': 5}, {'name': 're_phai', 'id': 6}, 
	{'name': 're_trai', 'id': 7}, {'name': 'di_thang', 'id': 8}, {'name': 'di_thang_or_re_phai', 'id': 9}, 
	{'name': 'di_thang_or_re_trai', 'id': 10}, {'name': 'huong_di_phai_theo_p', 'id': 11}, 
	{'name': 'huong_di_phai_theo_t', 'id': 12}]

#====MAIN
 
#Tao file label map
f = open(files['LABELMAP'], "w")
for label in labels:
	f.write('item { \n')
	f.write('\tname:\'{}\'\n'.format(label['name']))
	f.write('\tid:{}\n'.format(label['id']))
	f.write('}\n')

print(files['LABELMAP'])
print(os.path)