t = 5
vocabulary = {
    'Computer':'        n.คำนาม      คอมพิวเตอร์',
    'Guitar':'          n.คำนาม      กีต้าร์ ',
    'Punch':'           v.คำกริยา     ชก',
    'Run':'             v.คำกริยา     วิ่ง',
    'Rich':'            adj.คำขยายคำนาม   รวย',
}
while(True):
    print('พจนานุกรม\n 1)เพิ่มคำศัพท์\n 2)เเสดงคำศัพท์\n 3)ลบคำศัพท์\n 4)ออกจากโปรเเกรม\n')
    data = int(input('Input choice :'))
    if data == 1 :
        t += 1
        terminology = input('เพิ่มคำศัพท์\t:')
        type_word = input('ชนิดของคำ (ชนิดของคำ(n.,v.,adj.,adv.) :')
        if type_word == 'n.':
            type_word = 'n.คำนาม'
        elif type_word == 'v.':
            type_word = 'v.คำกริยา'
        elif type_word == 'adj.':
            type_word = 'adj.ขยายคำนาม.'
        elif type_word == 'adv.':
            type_word = 'adv. กริยาวิเศษณ์'
        meaning = input('ความหมาย\t :')
        vocabulary[terminology] =  '   '+type_word+'   '+meaning
        print('เพิ่มคำศัพท์เรียบร้อยเเล้ว')
    elif data == 2 :
        print(15*'-'+'\n คำศัพท์มีทั้งหมด ',t,' คำ\n',15*'-')
        print('คำศัพท์           ประเภท       ความหมาย')
        for i in vocabulary :
            print(i+vocabulary[i])
    elif data == 3 :
        delete = input('พิมพ์คำศัพท์ที่ตองการลบ :')
        x = input('ต้องการลบ'+delete+'ใช่หรือไม่ (yes / no):')
        if x == 'y':
            vocabulary.pop(delete)
            t -= 1
            print('ลบ'+delete+'เรียบร้อยเเล้ว')
    else:
        yes = input('ต้องการออกจากโปรเเกรมใช่หรือไม่ (yes / no):')
        if yes == ' yes':
            print('ออกจากโปรเเกรมเรียบร้อยเเล้ว')
            break