from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
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
        chieu_cao = request.form.get("chieu_cao", "").strip()
        can_nang = request.form.get("can_nang", "").strip()
        if chieu_cao == "":
            loi_cao = "Vui lòng nhập chiều cao."
        else:
            try:
                chieu_cao_so = float(chieu_cao.replace(",", "."))
                if chieu_cao_so < 50 or chieu_cao_so > 250:
                    loi_cao = "Chiều cao phải từ 50 đến 250 cm."
            except ValueError:
                loi_cao = "Vui lòng nhập một số."
        if can_nang == "":
            loi_nang = "Vui lòng nhập cân nặng."
        else:
            try:
                can_nang_so = float(can_nang.replace(",", "."))
                if can_nang_so < 10 or can_nang_so > 300:
                    loi_nang = "Cân nặng phải từ 10 đến 300 kg."
            except ValueError:
                loi_nang = "Vui lòng nhập một số."
        if loi_cao == "" and loi_nang == "":
            chieu_cao_met = chieu_cao_so / 100
            bmi_goc = can_nang_so / (chieu_cao_met ** 2)
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
if __name__ == "__main__":
    app.run(debug=True)