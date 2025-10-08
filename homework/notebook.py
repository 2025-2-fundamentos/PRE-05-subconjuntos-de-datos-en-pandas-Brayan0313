import pandas as pd  #  type: ignore
import pathlib

pd.set_option("display.notebook_repr_html", True)
# Carga del archivo desde un repo en GitHub
current_dir = pathlib.Path(__file__).parent
path = current_dir.parent / "files" / "input" / "truck_event_text_partition.csv"
truck_events = pd.read_csv(path)

# Cabecera del archivo
truck_events.head()
# Obtención de un subconjunto de registros
truck_events_subset = truck_events[0:10]
truck_events_subset
# Obtención de un subconjunto de columnas
specific_columns = truck_events_subset[["driverId", "eventTime", "eventType"]]
specific_columns
# Obtención de un subconjunto de filas y columnas
new_sub_set = truck_events.loc[0:10, ["driverId", "eventTime", "eventType"]]
new_sub_set
# Obtención de un campo de un registro en particular
truck_events.iloc[1]["driverName"]

# Escritura de la tabla en el disco
import os

if not os.path.exists(current_dir / "../files/output/"):
    os.makedirs(current_dir / "../files/output/")

specific_columns.to_csv(
    current_dir / "../files/output/specific-columns.csv",
    sep=",",
    header=True,
    index=False,
)