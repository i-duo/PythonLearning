import os.path
filename = 'studentInformation.txt'


def menu():
    print('\n=========================学生信息管理系统=========================')
    print('-----------------------------功能菜单-----------------------------')
    print('\t\t\t1. 录入学生信息')
    print('\t\t\t2. 查找学生信息')
    print('\t\t\t3. 删除学生信息')
    print('\t\t\t4. 修改学生信息')
    print('\t\t\t5. 排序')
    print('\t\t\t6. 统计学生总人数')
    print('\t\t\t7. 显示所有学生信息')
    print('\t\t\t0. 退出系统')
    print('==================================================================\n')


def main():
    while True:
        menu()
        while True:
            try:
                choice = int(input('请选择功能：'))
                if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
                    break
                else:
                    print('输入有误，请重新输入')
                    continue
            except ValueError:
                print('输入有误，请重新输入')
                continue
        if choice == 0:
            while True:
                answer = input('确定要退出系统吗？(y/n)')
                if answer == 'y' or answer == 'Y' or answer == 'n' or answer == 'N':
                    break
                else:
                    print('输入有误，请重新输入')
                    continue
            if answer == 'y' or answer == 'Y':
                print('谢谢使用')
                break
            elif answer == 'n' or answer == 'N':
                continue
        elif choice == 1:
            insert()
        elif choice == 2:
            search()
        elif choice == 3:
            delete()
        elif choice == 4:
            modify()
        elif choice == 5:
            sort()
        elif choice == 6:
            total()
        elif choice == 7:
            show()


def insert():
    student_list = []
    while True:
        while True:
            stu_id = input('请输入学生ID（如1001）：')
            if stu_id:
                break
            else:
                print('输入有误，请重新输入')
        while True:
            name = input('请输入学生姓名：')
            if name:
                break
            else:
                print('输入有误，请重新输入')
        while True:
            try:
                english = int(input('请输入英语成绩（整型）：'))
            except ValueError:
                print('输入有误，请重新输入')
                continue
            else:
                break
        while True:
            try:
                python = int(input('请输入Python成绩（整型）：'))
            except ValueError:
                print('输入有误，请重新输入')
                continue
            else:
                break
        while True:
            try:
                java = int(input('请输入Java成绩（整型）：'))
            except ValueError:
                print('输入有误，请重新输入')
                continue
            else:
                break
        student = {'id': stu_id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        print('学生信息录入成功')
        while True:
            answer = input('是否继续录入？(y/n)')
            if answer == 'y' or answer == 'Y' or answer == 'n' or answer == 'N':
                break
            else:
                print('输入有误，请重新输入')
                continue
        if answer == 'y' or answer == 'Y':
            continue
        elif answer == 'n' or answer == 'N':
            break
    with open(filename, 'a', encoding='utf-8') as aFile:
        for item in student_list:
            aFile.write(str(item) + '\n')


def search():
    student_query = []
    while True:
        stu_id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('请选择（1. 按ID查找 2. 按姓名查找）：')
            if mode == '1':
                while True:
                    stu_id = input('请输入学生ID：')
                    if stu_id == '':
                        print('输入有误，请重新输入')
                        continue
                    else:
                        break
            elif mode == '2':
                while True:
                    name = input('请输入学生姓名：')
                    if name == '':
                        print('输入有误，请重新输入')
                        continue
                    else:
                        break
            else:
                print('输入有误，请重新输入')
                continue
            with open(filename, 'r', encoding='utf-8') as rFile:
                student = rFile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if d['id'] == stu_id:
                        student_query.append(d)
                    if d['name'] == name:
                        student_query.append(d)
            if not student_query:
                print('无该学生信息')
            else:
                show_student(student_query)
            student_query.clear()
            while True:
                answer = input('是否继续查找？(y/n)')
                if answer == 'y' or answer == 'Y' or answer == 'n' or answer == 'N':
                    break
                else:
                    print('输入有误，请重新输入')
            if answer == 'y' or answer == 'Y':
                continue
            elif answer == 'n' or answer == 'N':
                break
        else:
            print('还没有录入学生信息')
            break


def show_student(lst):
    print('\n')
    format_title = '{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    format_data = '{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('english'))+int(item.get('python'))+int(item.get('java'))
                                 ))
    print('\n')


def modify():
    while True:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as rFile:
                student_old = rFile.readlines()
        else:
            print('还没有录入学生信息')
            return
        stu_id = ''
        name = ''
        flag = False
        while True:
            mode = input('请选择（1. 按ID修改 2. 按姓名修改）：')
            if mode == '1' or mode == '2':
                break
            else:
                print('输入有误，请重新输入')
                continue
        if mode == '1':
            while True:
                stu_id = input('请输入学生ID：')
                if stu_id == '':
                    print('输入有误，请重新输入')
                    continue
                else:
                    break
        elif mode == '2':
            while True:
                name = input('请输入学生姓名：')
                if name == '':
                    print('输入有误，请重新输入')
                    continue
                else:
                    break
        else:
            print('输入有误，请重新输入')
            continue
        with open(filename, 'w', encoding='utf-8') as wFile:
            for item in student_old:
                d = dict(eval(item))
                if d['id'] == stu_id or d['name'] == name:
                    print('已找到该学生的信息，可以进行修改')
                    while True:
                        while True:
                            where = input('请选择要修改的信息（1. ID 2. 姓名 3. 英语成绩 4. Python成绩 5. Java成绩）：')
                            if where not in ['1', '2', '3', '4', '5']:
                                print('输入有误，请重新输入')
                            else:
                                break
                        if where == '1':
                            while True:
                                a = input('请输入学生ID（如1001）：')
                                if a == '':
                                    print('输入有误，请重新输入')
                                else:
                                    d['id'] = a
                                    flag = True
                                    break
                        elif where == '2':
                            while True:
                                a = input('请输入学生姓名：')
                                if a == '':
                                    print('输入有误，请重新输入')
                                else:
                                    d['name'] = a
                                    flag = True
                                    break
                        elif where == '3':
                            while True:
                                try:
                                    a = int(input('请输入英语成绩（整型）：'))
                                except ValueError:
                                    print('输入有误，请重新输入')
                                    continue
                                else:
                                    d['english'] = a
                                    flag = True
                                    break
                        elif where == '4':
                            while True:
                                try:
                                    a = int(input('请输入Python成绩（整型）：'))
                                except ValueError:
                                    print('输入有误，请重新输入')
                                    continue
                                else:
                                    d['python'] = a
                                    flag = True
                                    break
                        elif where == '5':
                            while True:
                                try:
                                    a = int(input('请输入Java成绩（整型）：'))
                                except ValueError:
                                    print('输入有误，请重新输入')
                                    continue
                                else:
                                    d['java'] = a
                                    flag = True
                                    break
                        while True:
                            answer2 = input('是否修改其他信息？(y/n)')
                            if answer2 == 'y' or answer2 == 'Y' or answer2 == 'n' or answer2 == 'N':
                                break
                            else:
                                print('输入有误，请重新输入')
                                continue
                        if answer2 == 'y' or answer2 == 'Y':
                            continue
                        elif answer2 == 'n' or answer2 == 'N':
                            break
                    print('学生信息修改成功')
                    wFile.write(str(d) + '\n')
                else:
                    wFile.write(str(d) + '\n')
        if not flag:
            print('无该学生信息')
        while True:
            answer = input('是否修改其他学生信息？(y/n)')
            if answer == 'y' or answer == 'Y' or answer == 'n' or answer == 'N':
                break
            else:
                print('输入有误，请重新输入')
                continue
        if answer == 'y' or answer == 'Y':
            continue
        elif answer == 'n' or answer == 'N':
            break


def delete():
    while True:
        stu_id = ''
        name = ''
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                student_old = file.readlines()
            while True:
                mode = input('请选择（1. 按ID删除 2. 按姓名删除）：')
                if mode == '1' or mode == '2':
                    if mode == '1':
                        while True:
                            stu_id = input('请输入学生ID：')
                            if stu_id == '':
                                print('输入有误，请重新输入')
                                continue
                            else:
                                break
                    elif mode == '2':
                        while True:
                            name = input('请输入学生姓名：')
                            if name == '':
                                print('输入有误，请重新输入')
                            else:
                                break
                    break
                else:
                    print('输入有误，请重新输入')
                    continue
            flag = False
            with open(filename, 'w', encoding='utf-8') as wFile:
                for item in student_old:
                    d = dict(eval(item))
                    if d['id'] != stu_id and d['name'] != name:
                        wFile.write(str(d) + '\n')
                    else:
                        flag = True
            if flag:
                print('学生信息删除成功')
            else:
                print('无该学生信息')
        else:
            print('还没有录入学生信息')
            break
        while True:
            answer = input('是否继续删除？(y/n)')
            if answer == 'y' or answer == 'Y' or answer == 'n' or answer == 'N':
                break
            else:
                print('输入无效，请重新输入')
                continue
        if answer == 'y' or answer == 'Y':
            if len(student_old) == 1:
                print('还没有录入学生信息')
                return
            else:
                continue
        elif answer == 'n' or answer == 'N':
            break


def sort():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rFile:
            student_list = rFile.readlines()
        student_new = []
        for item in student_list:
            d = dict(eval(item))
            student_new.append(d)
        if not student_new:
            print('还没有录入学生信息')
            return
    else:
        print('还没有录入学生信息')
        return
    while True:
        asc_or_desc = '2'
        while asc_or_desc != '0' and asc_or_desc != '1':
            asc_or_desc = input('请选择（0. 升序 1. 降序）：')
            if asc_or_desc == '0':
                asc_or_desc_bool = False
            elif asc_or_desc == '1':
                asc_or_desc_bool = True
            else:
                print('输入有误，请重新输入')
                continue
        mode = 99
        while mode not in ['0', '1', '2', '3']:
            mode = input('请选择（1. 按英语成绩排序 2. 按Python成绩排序 3. 按Java成绩排序 0. 按总成绩排序）：')
            if mode == '1':
                student_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
            elif mode == '2':
                student_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
            elif mode == '3':
                student_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
            elif mode == '0':
                student_new.sort(key=lambda x: int(x['english'])+int(x['python'])+int(x['java']), reverse=asc_or_desc_bool)
            else:
                print('输入有误，请重新输入')
                continue
        show_student(student_new)
        while True:
            answer = input('是否进行其他排序？(y/n)')
            if answer == 'y' or answer == 'Y' or answer == 'n' or answer == 'N':
                break
            else:
                print('输入无效，请重新输入')
                continue
        if answer == 'y' or answer == 'Y':
            continue
        elif answer == 'n' or answer == 'N':
            break


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rFile:
            students = rFile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('还没有录入学生信息')


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rFile:
            students = rFile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
            else:
                print('还没有录入学生信息')
    else:
        print('还没有录入学生信息')


if __name__ == '__main__':
    main()
