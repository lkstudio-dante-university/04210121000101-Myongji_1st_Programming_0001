/** 회원 */
class CP01Member_08 {
	m_oID = "";
	m_oPassword = "";
	m_nGender = 0;
	m_oCommentList = [];

	/** 생성자 */
	constructor(a_oID, a_oPassword, a_nGender) {
		this.m_oID = a_oID;
		this.m_oPassword = a_oPassword;
		this.m_nGender = a_nGender;
	}

	/** 성별을 반환한다 */
	GetGender() {
		return (this.m_nGender <= 0) ? "남성" : "여성";
	}
}

/** 회원을 로드한다 */
function P01LoadMembers_08() {
	var oJSONStr = localStorage.getItem("Members");
	return (oJSONStr != null) ? JSON.parse(oJSONStr) : [];
}

/** 회원을 저장한다 */
function P01SaveMembers_08(a_oMemberList) {
	var oJSONStr = JSON.stringify(a_oMemberList);
	localStorage.setItem("Members", oJSONStr);
}

/** 회원을 탐색한다 */
function P01FindMember_08(a_oMemberList, a_oID) {
	for(var i = 0; i < a_oMemberList.length; ++i) {
		// 회원이 존재 할 경우
		if(a_oMemberList[i].m_oID == a_oID) {
			return i;
		}
	}

	return -1;
}
