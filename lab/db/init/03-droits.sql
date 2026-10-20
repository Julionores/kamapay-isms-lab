-- Moindre privilège pour le rôle applicatif (contrôles 8.2 et 8.3) :
-- lecture des clients, mise à jour du seul solde, insertion des transactions,
-- aucun droit DELETE, TRUNCATE ou DDL.
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public TO kamapay_app;

GRANT SELECT ON customers TO kamapay_app;
GRANT SELECT, UPDATE (balance) ON wallets TO kamapay_app;
GRANT SELECT, INSERT ON transactions TO kamapay_app;
GRANT USAGE ON SEQUENCE transactions_id_seq TO kamapay_app;
