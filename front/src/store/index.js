const initialState = {
    count: 23,
    boolNavBar: false,
    temp: 25,
    modalCreationProfil: false,
    modalProfil: false,
    profile: null
};


export default (storage, setStore, globalState) => {
    const store = {
        state: storage,
        'setState': setStore,
        merge: null,
    };

    const onces = [];

    store.merge = (obj) => {
        let newState = { ...store.state, ...obj };
        setStore(newState);
    }

    store.once = (f) => {
        onces.push(f);
    }


    store.start = () => {
        if (globalState.frist) {
            globalState.frist = false;
            onces.forEach(f => f());
        }
        
    }


    return store;
};

export {initialState};