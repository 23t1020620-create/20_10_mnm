
from flask import Flask, render_template, request

app = Flask(__name__)


# ================= TRANG CHỦ =================

@app.route("/")
def menu():
    return render_template("menu.html")


# ================= MÁY TÍNH =================

@app.route("/may-tinh", methods=["GET", "POST"])
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

        so_a = None
        so_b = None

        if not a:
            loi_a = "Vui lòng nhập số thứ nhất."
        else:
            try:
                so_a = float(a.replace(",", "."))
            except ValueError:
                loi_a = "Vui lòng nhập một số hợp lệ."

        if not b:
            loi_b = "Vui lòng nhập số thứ hai."
        else:
            try:
                so_b = float(b.replace(",", "."))
            except ValueError:
                loi_b = "Vui lòng nhập một số hợp lệ."

        if not loi_a and not loi_b:
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

    return render_template(
        "tinhToan.html",
        a=a,
        b=b,
        op=op,
        ket_qua=ket_qua,
        loi_a=loi_a,
        loi_b=loi_b,
        loi_op=loi_op
    )


# ================= KIỂM TRA ĐIỂM =================

def kiem_tra_diem(gia_tri):
    if gia_tri == "":
        return None, "Vui lòng nhập điểm."

    try:
        diem = float(gia_tri.replace(",", "."))
    except ValueError:
        return None, "Vui lòng nhập một số."

    if diem < 0 or diem > 10:
        return None, "Điểm phải từ 0 đến 10."

    return diem, ""


# ================= TÍNH ĐIỂM HỌC PHẦN =================

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

        if not loi_cc and not loi_gk and not loi_ck:

            diem_hp = round(
                diem_cc * 0.1 +
                diem_gk * 0.3 +
                diem_ck * 0.6,
                1
            )

            if diem_ck < 1:
                xep_loai = "F (điểm thi dưới 1)"

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

    return render_template(
        "diemTB.html",
        cc=cc,
        gk=gk,
        ck=ck,
        loi_cc=loi_cc,
        loi_gk=loi_gk,
        loi_ck=loi_ck,
        diem_hp=diem_hp,
        xep_loai=xep_loai
    )


# ================= TÍNH BMI =================

@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    chieu_cao = ""
    can_nang = ""

    loi_cao = ""
    loi_nang = ""

    bmi_value = None
    phan_loai = ""
    mau = ""
    can_nang_goi_y = ""

    if request.method == "POST":

        chieu_cao = request.form.get(
            "chieu_cao", ""
        ).strip()

        can_nang = request.form.get(
            "can_nang", ""
        ).strip()

        chieu_cao_so = None
        can_nang_so = None

        if not chieu_cao:
            loi_cao = "Vui lòng nhập chiều cao."
        else:
            try:
                chieu_cao_so = float(
                    chieu_cao.replace(",", ".")
                )

                if not 50 <= chieu_cao_so <= 250:
                    loi_cao = "Chiều cao phải từ 50 đến 250 cm."

            except ValueError:
                loi_cao = "Vui lòng nhập một số."

        if not can_nang:
            loi_nang = "Vui lòng nhập cân nặng."
        else:
            try:
                can_nang_so = float(
                    can_nang.replace(",", ".")
                )

                if not 10 <= can_nang_so <= 300:
                    loi_nang = "Cân nặng phải từ 10 đến 300 kg."

            except ValueError:
                loi_nang = "Vui lòng nhập một số."

        if not loi_cao and not loi_nang:

            chieu_cao_met = chieu_cao_so / 100

            bmi_goc = can_nang_so / (
                chieu_cao_met ** 2
            )

            bmi_value = round(bmi_goc, 1)

            if bmi_goc < 18.5:
                phan_loai = "Thiếu cân"
                mau = "vang"

            elif bmi_goc < 23:
                phan_loai = "Bình thường"
                mau = "xanh"

            elif bmi_goc < 25:
                phan_loai = "Thừa cân"
                mau = "vang"

            else:
                phan_loai = "Béo phì"
                mau = "do"

            can_min = 18.5 * (chieu_cao_met ** 2)
            can_max = 22.9 * (chieu_cao_met ** 2)

            can_nang_goi_y = (
                f"{can_min:.1f} – {can_max:.1f} kg"
            )

    return render_template(
        "bmi.html",
        chieu_cao=chieu_cao,
        can_nang=can_nang,
        loi_cao=loi_cao,
        loi_nang=loi_nang,
        bmi_value=bmi_value,
        phan_loai=phan_loai,
        mau=mau,
        can_nang_goi_y=can_nang_goi_y
    )


# ================= CHẠY ỨNG DỤNG =================

if __name__ == "__main__":
    app.run(debug=True)
