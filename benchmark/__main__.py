import parahash.md5 as pmd5
import torch
import time


def benchmark_md5():
    # device = "cuda"
    device = "cpu"
    batch = 2**20
    data = torch.zeros(batch, 4, dtype=torch.int64, device=device)
    data, blocks = pmd5.preprocess(data, torch.full(
        (batch,), 128, dtype=torch.int64, device=device))
    start = time.time()
    pmd5.md5_preprocessed(data, blocks)
    print(f"HPS: {batch/(time.time()-start):.2f}")


def main():
    benchmark_md5()


if __name__ == "__main__":
    main()
