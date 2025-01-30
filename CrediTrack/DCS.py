# PRUNA, DE GUZMAN, DORONGON
# BET-COET-2A
# CPET 5L PRELIM
# CREDITRACK

import sys
import json
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class DebtCollectorSystem(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.load_data()
        self.show_front_ui()
        self.setWindowTitle("CrediTract")

    def load_data(self):
        with open("data.json", "r") as file:
            self.data = json.load(file)

    def fade_in(self, widget):
        self.animation = QtCore.QPropertyAnimation(widget, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def fade_out(self, widget):
        self.animation = QtCore.QPropertyAnimation(widget, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(1)
        self.animation.setEndValue(0)
        self.animation.finished.connect(widget.hide)
        self.animation.start()

    def show_front_ui(self):
        if hasattr(self, 'front_ui'):
            self.fade_out(self.front_ui)
            self.front_ui.hide()
        if hasattr(self, 'dashboard_ui'):
            self.fade_out(self.dashboard_ui)
            self.dashboard_ui.hide()
        self.front_ui = uic.loadUi("ui/front.ui", self)
        self.front_ui.Service.clicked.connect(self.show_dashboard)
        self.front_ui.About.clicked.connect(self.show_help)
        self.front_ui.Next.clicked.connect(self.show_dashboard)
        self.front_ui.setFixedSize(self.front_ui.size())
        self.front_ui.show()
        self.fade_in(self.front_ui)
        self.setWindowTitle("CrediTract")

    def show_dashboard(self):
        if hasattr(self, 'front_ui'):
            self.fade_out(self.front_ui)
            self.front_ui.hide()
        self.dashboard_ui = uic.loadUi("ui/Dashboard.ui", self)
        self.populate_dashboard()
        self.create_charts()
        self.dashboard_ui.Previous.clicked.connect(self.show_front_ui)  # Ensure this is connected correctly
        self.dashboard_ui.Next.clicked.connect(self.show_list_ui)
        self.dashboard_ui.setFixedSize(self.dashboard_ui.size())
        self.dashboard_ui.show()
        self.fade_in(self.dashboard_ui)
        self.setWindowTitle("CrediTract")

    def populate_dashboard(self):
        debtor_data = self.data["debtors"]
        total_owed = sum(debtor["total_debt"] for debtor in debtor_data)
        self.dashboard_ui.dashboard_table.setRowCount(len(debtor_data))
        self.dashboard_ui.owed_label.setText(f"Total Owed: {total_owed}")

        for i, debtor in enumerate(debtor_data):
            self.dashboard_ui.dashboard_table.setItem(i, 0, QtWidgets.QTableWidgetItem(debtor["name"]))
            self.dashboard_ui.dashboard_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(debtor["total_debt"])))
            self.dashboard_ui.dashboard_table.setItem(i, 2, QtWidgets.QTableWidgetItem(str(debtor["overdue_payments"])))

    def create_charts(self):
        chart_widget = QtWidgets.QWidget(self.dashboard_ui)
        layout = QVBoxLayout(chart_widget)
        self.create_pie_chart(layout)
        self.dashboard_ui.chart_layout.addWidget(chart_widget)

    def create_pie_chart(self, layout):
        debtor_data = self.data["debtors"]
        sizes = [debtor["total_debt"] for debtor in debtor_data]
        colors = plt.cm.Paired(np.arange(len(sizes)))

        fig, ax = plt.subplots(figsize=(54, 50))

        wedges, _, autotexts = ax.pie(
            sizes,
            colors=colors,
            startangle=90,
            wedgeprops=dict(width=0.4),
            autopct='%1.1f%%',
            pctdistance=0.75
        )

        for autotext in autotexts:
            autotext.set_fontsize(7)

        centre_circle = plt.Circle((0, 0), 0.70, fc='none')
        ax.add_artist(centre_circle)
        ax.axis('equal')

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()

    def show_list_ui(self):
        if hasattr(self, 'dashboard_ui'):
            self.fade_out(self.dashboard_ui)
            self.dashboard_ui.hide()
        self.list_ui = uic.loadUi("ui/List.ui", self)
        self.populate_list_ui()
        self.list_ui.Previous.clicked.connect(self.show_dashboard)  # Ensure this is connected correctly
        self.list_ui.Next.clicked.connect(self.show_information_ui)
        self.list_ui.setFixedSize(self.list_ui.size())
        self.list_ui.show()
        self.fade_in(self.list_ui)
        self.setWindowTitle("CrediTract")

    def populate_list_ui(self):
        debtor_data = self.data["debtors"]
        self.list_ui.List.setRowCount(len(debtor_data))

        for i, debtor in enumerate(debtor_data):
            self.list_ui.List.setItem(i, 0, QtWidgets.QTableWidgetItem(debtor.get("name", "N/A")))
            self.list_ui.List.setItem(i, 1, QtWidgets.QTableWidgetItem(str(debtor.get("total_debt", 0))))
            due_date = debtor["payment_schedule"][0]["due_date"] if debtor["payment_schedule"] else "N/A"
            self.list_ui.List.setItem(i, 2, QtWidgets.QTableWidgetItem(due_date))
            self.list_ui.List.setItem(i, 3, QtWidgets.QTableWidgetItem(debtor.get("interest_calculation", "N/A")))
            self.list_ui.List.setItem(i, 4, QtWidgets.QTableWidgetItem(str(debtor.get("overdue_payments", 0))))
            self.list_ui.List.setItem(i, 5, QtWidgets.QTableWidgetItem(debtor.get("notes", "N/A")))

    def show_information_ui(self):
        if hasattr(self, 'list_ui'):
            self.fade_out(self.list_ui)
            self.list_ui.hide()
        self.information_ui = uic.loadUi("ui/Information.ui", self)
        self.populate_information_ui()
        self.information_ui.Previous.clicked.connect(self.show_list_ui)  # Ensure this is connected correctly
        self.information_ui.Next.clicked.connect(self.show_notification_ui)
        self.information_ui.setFixedSize(self.information_ui.size())
        self.information_ui.show()
        self.fade_in(self.information_ui)
        self.setWindowTitle("CrediTract")

    def populate_information_ui(self):
        debtor_data = self.data["debtors"]
        self.information_ui.payment_history.setRowCount(len(debtor_data))
        self.information_ui.payment_schedule.setRowCount(len(debtor_data))
        self.information_ui.interest_cal.setRowCount(len(debtor_data))
        self.information_ui.note.setRowCount(len(debtor_data))

        for i, debtor in enumerate(debtor_data):
            for j, payment in enumerate(debtor["payment_history"]):
                self.information_ui.payment_history.setItem(i, 0, QtWidgets.QTableWidgetItem(payment.get("date_paid", "")))
                self.information_ui.payment_history.setItem(i, 1, QtWidgets.QTableWidgetItem(str(payment.get("amount_paid", ""))))
                self.information_ui.payment_history.setItem(i, 2, QtWidgets.QTableWidgetItem(payment.get("payment_method", "")))

            for k, schedule in enumerate(debtor["payment_schedule"]):
                self.information_ui.payment_schedule.setItem(i, 0, QtWidgets.QTableWidgetItem(schedule.get("due_date", "")))
                self.information_ui.payment_schedule.setItem(i, 1, QtWidgets.QTableWidgetItem(str(schedule.get("total_debt", ""))))
                self.information_ui.payment_schedule.setItem(i, 2, QtWidgets.QTableWidgetItem(schedule.get("status", "")))

            self.information_ui.interest_cal.setItem(i, 0, QtWidgets.QTableWidgetItem(debtor["name"]))
            self.information_ui.interest_cal.setItem(i, 1, QtWidgets.QTableWidgetItem(debtor["interest_calculation"]))
            self.information_ui.note.setItem(i, 0, QtWidgets.QTableWidgetItem(debtor["notes"]))

    def show_notification_ui(self):
        if hasattr(self, 'information_ui'):
            self.fade_out(self.information_ui)
            self.information_ui.hide()
        self.notification_ui = uic.loadUi("ui/Notification.ui", self)
        self.populate_notification_ui()
        self.notification_ui.Previous.clicked.connect(self.show_information_ui)  # Ensure this is connected correctly
        self.notification_ui.Next.clicked.connect(self.show_end_ui)
        self.notification_ui.setFixedSize(self.notification_ui.size())
        self.notification_ui.show()
        self.fade_in(self.notification_ui)
        self.setWindowTitle("CrediTract")

    def populate_notification_ui(self):
        self.notification_ui.upcoming_events.setRowCount(5)
        self.notification_ui.overdue_accounts.setRowCount(len(self.data["debtors"]))
        self.notification_ui.interest_penalties.setRowCount(len(self.data["notifications"].get("interest_penalties", [])))
        upcoming_events = self.data["notifications"].get("upcoming_events", [])
        for i in range(min(5, len(upcoming_events))):  # Limit to 5 rows
            self.notification_ui.upcoming_events.setItem(i, 0, QtWidgets.QTableWidgetItem(upcoming_events[i]))

        for i, debtor in enumerate(self.data["debtors"]):
            if debtor["overdue_payments"] > 0:
                self.notification_ui.overdue_accounts.setItem(i, 0, QtWidgets.QTableWidgetItem(debtor["name"]))
                self.notification_ui.interest_penalties.setItem(i, 0, QtWidgets.QTableWidgetItem(debtor["name"]))
                self.notification_ui.interest_penalties.setItem(i, 1, QtWidgets.QTableWidgetItem("Active"))  # Example status
                penalty_amount = str(debtor["total_debt"] * 0.05)  # Assuming penalty is 5% of total debt
                self.notification_ui.interest_penalties.setItem(i, 2, QtWidgets.QTableWidgetItem(penalty_amount)) 

        for j, penalty in enumerate(self.data["notifications"].get("interest_penalties", [])):
            self.notification_ui.interest_penalties.setItem(j, 0, QtWidgets.QTableWidgetItem(penalty["name"]))
            self.notification_ui.interest_penalties.setItem(j, 1, QtWidgets.QTableWidgetItem(penalty["status"]))
            self.notification_ui.interest_penalties.setItem(j, 2, QtWidgets.QTableWidgetItem(penalty["penalties"]))

        self.notification_ui.upcoming_events.update()
        self.notification_ui.overdue_accounts.update()
        self.notification_ui.interest_penalties.update()

    def show_end_ui(self):
        if hasattr(self, 'notification_ui'):
            self.fade_out(self.notification_ui)
            self.notification_ui.hide()
        self.end_ui = uic.loadUi("ui/End.ui", self)
        self.end_ui.setFixedSize(self.end_ui.size())
        self.end_ui.show()
        self.fade_in(self.end_ui)
        QTimer.singleShot(3000, self.close_application)
        self.setWindowTitle("CrediTract")

    def close_application(self):
        self.close()

    def show_help(self):
        if hasattr(self, 'front_ui'):
            self.front_ui.hide()
        self.help_ui = uic.loadUi("ui/Help.ui", self)
        self.help_ui.Previous.clicked.connect(self.show_front_ui)
        self.help_ui.show() 
        self.setWindowTitle("CrediTract")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DebtCollectorSystem()
    window.setWindowTitle("CrediTract")  
    window.show()  
    sys.exit(app.exec_())

