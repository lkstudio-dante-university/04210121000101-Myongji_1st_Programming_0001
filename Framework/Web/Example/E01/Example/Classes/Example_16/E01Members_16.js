/*
window 객체의 onload 속성은 웹 브라우저가 로드 되었을 때 호출 될 메서드를 지정하는 역할을 수행한다. (즉, 웹 문서가 로드 되었을 때 특정 데이터로
초기화하고 싶을 경우 해당 속성을 활용하면 된다는 것을 알 수 있다.)
*/
window.onload = function() {
	var oJSONStr = localStorage.getItem("Members");

	// 회원 정보가 없을 경우
	if(oJSONStr == null || oJSONStr.length <= 0) {
		return;
	}

	var oMemberList = JSON.parse(oJSONStr);
	
	for(var i = 0; i < oMemberList.length; ++i) {
		AddMember(i + 1, oMemberList[i]);
	}
}

/** 회원을 추가한다 */
function AddMember(a_nNum, a_oMember) {
	var oTable = document.getElementById("Members");
	var oTableRow = document.createElement("tr");

	var oNumTableCol = document.createElement("td");
	oNumTableCol.appendChild(document.createTextNode(a_nNum));

	var oIDTableCol = document.createElement("td");
	oIDTableCol.appendChild(document.createTextNode(a_oMember.m_oID));

	var oPasswordTableCol = document.createElement("td");
	oPasswordTableCol.appendChild(document.createTextNode(a_oMember.m_oPassword));

	oTableRow.appendChild(oNumTableCol);
	oTableRow.appendChild(oIDTableCol);
	oTableRow.appendChild(oPasswordTableCol);

	oTable.appendChild(oTableRow);
}