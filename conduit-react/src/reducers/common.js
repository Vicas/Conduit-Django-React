const defaultState= {
  appName: 'Conduit',
  token: null
};

export default (state = defaultState, action) => {
  switch (action.type) {
    case 'APP_LOAD':
      return {
        ...state,
        token: action.token || null,
        appLoaded: true,
        currentUser: action.payload ? action.payload.user : null
      };
    case 'REDIRECT':
      return { ...state, redirectTo: null };
    case 'LOGOUT':
      return { ...state, redirectTo: '/', token: null, currentUser: null };
    case 'ARTICLE_SUBMITTED':
      const redirectUrl = `article/${action.payload.article.slug}`;
      return { ...state, redirectTo: redirectUrl };
    case 'SETTINGS_SAVED':
      return {
        ...state,
        redirectTo: action.error ? null : '/',
        currentUser: action.error ? null : action.payload.user
      };
    // Logins and registrations should both update the state with token and currentUser info
    case 'LOGIN':
    case 'REGISTER':
      return {
        ...state,
        redirectTo: action.error ? null : '/',
        token: action.error ? null: action.payload.user.token,
        currentUser: action.error ? null : action.payload.user
      };
    case 'DELETE_ARTICLE':
      return { ...state, redirectTo: '/' };
    default:
  }
  return state;
};