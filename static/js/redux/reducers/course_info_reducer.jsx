export const courseInfo = (state = {isFetching: true, data: {}, id: null}, action) => {
	switch (action.type) {
		case "COURSE_INFO_RECEIVED":
			return {
				isFetching: false,
				data: action.data,
				id: action.data.id
			};
		case "REQUEST_COURSE_INFO":
			return {
				isFetching: true,
				data: {},
				id: action.id
			};
		case "SET_COURSE_REACTIONS":
			if (state.id === null) {
				return state;
			}
			return Object.assign({}, state,
			{
				data: Object.assign({}, state.data, {
					reactions: action.reactions
				})
			});
		case "SET_COURSE_ID":
			return Object.assign({}, state, {id: action.id})
		default: 
			return state;
	}
}