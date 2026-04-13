#![no_std]

use soroban_sdk::{contract, contractimpl, contracttype, Address, Env, String, Vec};

#[contracttype]
#[derive(Clone)]
pub enum DataKey {
    Admin,
    AuthorizedIndexer(Address),
}

#[contracttype]
#[derive(Clone, Debug, Eq, PartialEq)]
pub struct EventRecord {
    pub contract_id: String,
    pub event_type: String,
    pub payload: String,
    pub ledger: u32,
    pub timestamp: u64,
    pub indexer: Address,
}

#[contract]
pub struct Learn2Earn SorobanCore;

#[contractimpl]
impl Learn2Earn SorobanCore {
    pub fn initialize(env: Env, admin: Address) {
        if env.storage().instance().has(&DataKey::Admin) {
            panic!("already initialized")
        }
        admin.require_auth();
        env.storage().instance().set(&DataKey::Admin, &admin);
    }

    pub fn set_indexer(env: Env, indexer: Address, allowed: bool) {
        let admin: Address = env
            .storage()
            .instance()
            .get(&DataKey::Admin)
            .expect("not initialized");
        admin.require_auth();
        env.storage()
            .persistent()
            .set(&DataKey::AuthorizedIndexer(indexer), &allowed);
    }

    pub fn emit_event(
        env: Env,
        indexer: Address,
        contract_id: String,
        event_type: String,
        payload: String,
        ledger: u32,
        timestamp: u64,
    ) {
        indexer.require_auth();
        let allowed = env
            .storage()
            .persistent()
            .get::<_, bool>(&DataKey::AuthorizedIndexer(indexer.clone()))
            .unwrap_or(false);
        if !allowed {
            panic!("unauthorized indexer")
        }

        let record = EventRecord {
            contract_id,
            event_type,
            payload,
            ledger,
            timestamp,
            indexer,
        };

        env.events()
            .publish((String::from_str(&env, "learn2earn-soroban"),), record);
    }

    pub fn is_indexer(env: Env, indexer: Address) -> bool {
        env.storage()
            .persistent()
            .get::<_, bool>(&DataKey::AuthorizedIndexer(indexer))
            .unwrap_or(false)
    }

    pub fn get_admin(env: Env) -> Address {
        env.storage()
            .instance()
            .get(&DataKey::Admin)
            .expect("not initialized")
    }

    pub fn supported_events(env: Env) -> Vec<String> {
        Vec::from_array(
            &env,
            [
                String::from_str(&env, "transfer"),
                String::from_str(&env, "mint"),
                String::from_str(&env, "burn"),
                String::from_str(&env, "custom"),
            ],
        )
    }
}
