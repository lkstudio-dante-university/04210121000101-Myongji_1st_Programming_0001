/** 회원 버튼을 눌렀을 경우 */
function OnTouchMemberShipBtn(a_bIsJoin) {
	// 회원 가입 상태 일 경우
	if(a_bIsJoin) {
		HandleJoinState();
	} else {
		HandleClearState();
	}
}

/** 가입 상태를 처리한다 */
function HandleJoinState() {
	var oID = document.getElementById("ID");
	var oPassword = document.getElementById("Password");

	// 입력 필드가 유효하지 않을 경우
	if(oID.value.length <= 0 || oPassword.value.length <= 0) {
		alert("아이디 or 비밀번호를 입력해주세요.");
	} else {
		var oSavedID = localStorage.getItem("ID");
		var oSavedPassword = localStorage.getItem("Password");

		// 아이디가 존재 할 경우
		if(oSavedID == oID.value) {
			alert("아이디가 존재합니다.");
		} else {
			localStorage.setItem("ID", oID.value);
			localStorage.setItem("Password", oPassword.value);

			alert("회원 가입에 성공했습니다.");
		}
	}
}

/** 지우기 상태를 처리한다 */
function HandleClearState() {
	localStorage.clear();
}
