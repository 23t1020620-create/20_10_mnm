from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def may_tinh():
    a = ""
    b = ""
    op = "+"
    ket_qua = None
    loi_a = ""
    loi_b = ""
    loi_op = ""
    if request.method == "POST":
        a = request.form.get("a", "").strip()
        b = request.form.get("b", "").strip()
        op = request.form.get("op", "+")
        if a == "" and b == "":
            loi_a = "Vui lòng nhập số thứ nhất."
            loi_b = "Vui lòng nhập số thứ hai."
        elif a == "":
            loi_a = "Vui lòng nhập số thứ nhất."
        elif b == "":
            loi_b = "Vui lòng nhập số thứ hai."
        else:
            try:
                so_a = float(a.replace(",", "."))
            except ValueError:
                loi_a = "Vui lòng nhập một số hợp lệ."
            try:
                so_b = float(b.replace(",", "."))
            except ValueError:
                loi_b = "Vui lòng nhập một số hợp lệ."
            if loi_a == "" and loi_b == "":
                if op not in ["+", "-", "*", "/"]:
                    loi_op = "Phép toán không hợp lệ."
                elif op == "+":
                    ket_qua = so_a + so_b
                elif op == "-":
                    ket_qua = so_a - so_b
                elif op == "*":
                    ket_qua = so_a * so_b
                elif op == "/":
                    if so_b == 0:
                        loi_b = "Không thể chia cho 0."
                    else:
                        ket_qua = so_a / so_b
    return render_template("tinhToan.html",a=a,b=b,op=op,ket_qua=ket_qua,loi_a=loi_a,loi_b=loi_b,loi_op=loi_op)

def kiem_tra_diem(gia_tri):
    if gia_tri == "":
        return None, "Vui long nhap diem."
    try:
        diem = float(gia_tri.replace(",", "."))
    except ValueError:
        return None, "Vui long nhap mot so."
    if diem < 0 or diem > 10:
        return None, "Diem phai tu 0 den 10."
    return diem, ""

@app.route("/DTB", methods=["GET", "POST"])
def tinh_diem():
    cc = ""
    gk = ""
    ck = ""
    loi_cc = ""
    loi_gk = ""
    loi_ck = ""
    diem_hp = None
    xep_loai = ""
    if request.method == "POST":
        cc = request.form.get("cc", "").strip()
        gk = request.form.get("gk", "").strip()
        ck = request.form.get("ck", "").strip()
        diem_cc, loi_cc = kiem_tra_diem(cc)
        diem_gk, loi_gk = kiem_tra_diem(gk)
        diem_ck, loi_ck = kiem_tra_diem(ck)
        if loi_cc == "" and loi_gk == "" and loi_ck == "":
            diem_hp = round(diem_cc * 0.1+ diem_gk * 0.3+ diem_ck * 0.6 , 1)
            if diem_ck < 1:
                xep_loai = "F (diem thi duoi 1)"
            elif diem_hp >= 8.5:
                xep_loai = "A"
            elif diem_hp >= 7.0:
                xep_loai = "B"
            elif diem_hp >= 5.5:
                xep_loai = "C"
            elif diem_hp >= 4.0:
                xep_loai = "D"
            else:
                xep_loai = "F"
    return render_template("diemTB.html", cc=cc, gk=gk, ck=ck, loi_cc=loi_cc, loi_gk=loi_gk, loi_ck=loi_ck, diem_hp=diem_hp, xep_loai=xep_loai)
if __name__ == "__main__":
    app.run(debug=True)
