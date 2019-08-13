import QtQuick.Window 2.2 as UQml
import QtQuick 2.7
import "qmls" as Uqmls
import "jscripts/u_js.js" as Ujs
  UQml.Window {
    visible: true
    width: 500
    height: 300
    title: qsTr("Sixth Qml")
    color: "#000F1F"
    Uqmls.UCircle {
        id: rcircle
	width: 140
        height: 140
        anchors.centerIn: parent
        MouseArea {
	    anchors.fill: parent
	    onClicked: rcircle.height = Ujs.hsize(rcircle.height);
        }
    }
    Uqmls.URect {
        id: rect1
        property int rzwidth: parent.width - (parent.width/5)
        signal colored(color uColor)
        color: "#000000"
        width: parent.width - (parent.width / 5)
        height: parent.height/10
        onColored: rect1.color = uColor;
        MouseArea {
            id: mareal
            anchors.fill: parent
        }
        Connections {
            target: mareal 
            onClicked: {
                    rect1.width = rect1.rzwidth;
                    rect2.visible = true;
        	}
            onPressed: rect1.colored("#002737")
	}
    }
    Uqmls.URect {
        id: rect2
        color: "#00293b"
        x: rect1.width
        visible: false
        width: parent.width / 5 
        height: parent.height
        MouseArea {
            anchors.fill: parent
            onClicked: {
               rect2.visible =  false;
               rect2.color = "#340147";
               utext2.text = "text 2";
               utext3.text = "text 3";
            }
        }
        Uqmls.UButton {
                id: ubut1
		text: "Hide"
                width: rect2.width
                height: rect2.height/10
                onClicked: {
                rect2.visible = false;
                rect1.width = UQml.Window.width;
            }
	}
    }
    Uqmls.UText {
            id: utext1
            x: 20
            y: 50
            font.family: "Open"
            font.pixelSize: 37
            width: rect1.width - (20 * 2)
            text: "text 1"
    }
    Uqmls.UText {
            id: utext2
            x: 20
            y: utext1.height + (50 * 2)
            font.family: "Verdana"
            font.pixelSize: 27
            width: rect1.width - (20 * 2) 
    }
    Uqmls.UText {
            id: utext3
            x: 20
            y: (utext1.height + utext2.height) + (50 * 3)
            font.family: "Open Sans"
            font.pointSize: 14
            width: rect1.width - (20 * 2)
    }
}
