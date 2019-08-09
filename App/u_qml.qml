import QtQuick 2.7 as UQml
import QtQuick.Window 2.2 as UQml

  UQml.Window {
    visible: true
    width: 350
    height: 590
    title: qsTr("Second Qml")
    UQml.Rectangle {
	color: "#FF0000"
	width: 140
        height: 140
	border.color: "#FF00FF"
	border.width: 5
        radius: width*0.5
    }
}
