# import pytest
# import model
# import orm
# from sqlalchemy import insert, text
# from sqlalchemy.orm import Session
# import repository

# @pytest.skip(reason="")
# def test_repository_can_save_a_batch(session: Session):
#     batch = model.Batch("batch1", "RUSTY-SOAPDISH", 100, eta=None)

#     repo = repository.SQLAlchemyRepository(session)
#     repo.add(batch)
#     session.commit()

#     rows = list(session.execute(text(
#         "SELECT reference, sku, _purchased_quantity, eta FROM batches"
#     )))
#     assert rows == [("batch1", "RUSTY-SOAPDISH", 100, eta=None),]

# @pytest.skip(reason="")
# def insert_order_line(session: Session):
#     # session.execute(text(
#     #     "INSERT INTO order_lines (orderid, sky, qty)"
#     #     "VALUES (order1, GENERIC-SOFA, 12)"
#     # ))
#     session.execute(insert(orm.orde
#     [[orderline_id]] = session.execute(text(
#         "SELECT id FROM order_lines WHERE orderid=:orderid AND sku=:sky"
#     ), dict(orderid="order1", sku="GNERIC-SOFA"))
#     return orderline_id
    