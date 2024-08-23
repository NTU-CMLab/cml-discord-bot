BIND_CANNOT_FIND_ACCOUNT = '''
Hi {},

我們無法在 CMLab 資料庫找到您輸入的帳號 (`{}`)

'''

BIND_DIFFERENT_NAME = '''
Hi {},

您似乎還沒有按照群組規則命名您的 Discord 名稱
    or
資料庫紀錄 {} 的姓名與您目前的 Discord 並不相同:

    > [學號前三碼]-[姓名]， 例如: R13-王小明

如果修改過後仍然存在問題請找網管。
您可以透過 DC 聯絡網管或 mail 到 unix_manager@cmlab.csie.ntu.edu.tw

'''

BIND_SUCCESS = '''
Hi {},

我們從資料庫找到您屬於 `{} group`, 因此會幫您分配到 Discord `{}` 的身份！
同時我們也已經綁定您的 CMLab 使用者帳號 `{}`，未來我們能夠透過自動化工具提供給您相關通知！

'''

BIND_GROUP_ERROR = '''
Hi {},

我們在幫您分組時出現了一點錯誤，請聯絡網管！
您可以透過 DC 聯絡網管或 mail 到 unix_manager@cmlab.csie.ntu.edu.tw

'''
BIND_BINDED = '''
Hi {},

這個使用者帳號 `{}` 已經綁定過 Discord 帳號！
您可以透過 DC 聯絡網管或 mail 到 unix_manager@cmlab.csie.ntu.edu.tw
'''
